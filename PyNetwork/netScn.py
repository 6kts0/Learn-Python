import subprocess
import socket
import struct
import ipaddress
import concurrent.futures
import time
import os
import csv
import sys
from datetime import datetime
from scapy.all import ARP, Ether, srp, conf

conf.verb = 0  # silence scapy

# Return scan origin's LAN IP address
def get_local_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

# Return the /24 network
def get_subnet(ip, prefix=24):
    net = ipaddress.IPv4Network(f"{ip}/{prefix}", strict=False)
    return str(net)

def resolve_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror):
        return ip

def arp_scan(subnet):
    """
    Layer-2 ARP sweep. Fast and reliable, but requires admin/root
    and only works on the local broadcast domain.
    """
    arp_req = ARP(pdst=subnet)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    answered, _ = srp(ether / arp_req, timeout=2, verbose=False)

    devices = []
    for _, rcv in answered:
        ip = rcv.psrc
        mac = rcv.hwsrc
        devices.append({'ip': ip, 'mac': mac, 'hostname': resolve_hostname(ip)})
    return devices


def ping_host(ip):
    """
    Pings a single device. Returns IP string if host is alive, else None.
    Cross-platform (Windows vs *nix flags).
    """
    if os.name == 'nt':
        cmd = ['ping', '-n', '1', '-w', '500', str(ip)]
    else:
        cmd = ['ping', '-c', '1', '-W', '1', str(ip)]
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return str(ip) if result.returncode == 0 else None


def get_mac_from_arp_table(ip):
    """
    Pull MAC for ip from the OS ARP cache after a successful ping.
    """
    try:
        out = subprocess.check_output(['arp', '-a', ip], stderr=subprocess.DEVNULL, text=True)
        for line in out.splitlines():
            parts = line.split()
            for i, p in enumerate(parts):
                # MAC formats: aa:bb:cc:dd:ee:ff or aa-bb-cc-dd-ee-ff
                if len(p) == 17 and (p.count(':') == 5 or p.count('-') == 5):
                    return p.replace('-', ':').lower()
    except subprocess.CalledProcessError:
        pass
    return 'unknown'


def ping_sweep(subnet):
    """
    Fallback ping sweep + ARP lookup in case L2 ARP scan fails
    (e.g. running without privileges, or scanning across a router).
    """
    hosts = list(ipaddress.IPv4Network(subnet, strict=False).hosts())

    print(f"  Pinging {len(hosts)} hosts in parallel...")
    alive = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=64) as pool:
        for ip in pool.map(ping_host, hosts):
            if ip:
                alive.append(ip)

    devices = []
    for ip in sorted(alive, key=lambda x: ipaddress.IPv4Address(x)):
        devices.append({
            'ip': ip,
            'mac': get_mac_from_arp_table(ip),
            'hostname': resolve_hostname(ip),
        })
    return devices


def merge_results(primary, secondary):
    """Merge two device lists, preferring entries from `primary` when IPs collide."""
    by_ip = {d['ip']: d for d in secondary}
    for d in primary:
        existing = by_ip.get(d['ip'], {})
        # prefer non-'unknown' MACs and real hostnames
        merged = {
            'ip': d['ip'],
            'mac': d['mac'] if d.get('mac') and d['mac'] != 'unknown' else existing.get('mac', 'unknown'),
            'hostname': d['hostname'] if d.get('hostname') and d['hostname'] != d['ip'] else existing.get('hostname', d['ip']),
        }
        by_ip[d['ip']] = merged
    return sorted(by_ip.values(), key=lambda x: ipaddress.IPv4Address(x['ip']))


def print_table(devices):
    if not devices:
        print("\nNo live hosts found.")
        return
    print(f"\n{'IP Address':<16} {'MAC Address':<20} {'Hostname'}")
    print("-" * 70)
    for d in devices:
        print(f"{d['ip']:<16} {d['mac']:<20} {d['hostname']}")
    print(f"\nTotal: {len(devices)} device(s)")


def save_csv(devices, path):
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['ip', 'mac', 'hostname'])
        writer.writeheader()
        writer.writerows(devices)
    print(f"Results saved to {path}")


def main():
    start = time.time()
    local_ip = get_local_ip()
    subnet = get_subnet(local_ip)

    print(f"Network Scanner — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Local IP : {local_ip}")
    print(f"Subnet   : {subnet}\n")

    # 1) Try fast L2 ARP scan first
    arp_results = []
    try:
        print("[1/2] Running ARP scan...")
        arp_results = arp_scan(subnet)
        print(f"      Found {len(arp_results)} host(s) via ARP.")
    except PermissionError:
        print("      ARP scan needs admin/root privileges — skipping.")
    except Exception as e:
        print(f"      ARP scan failed ({e}) — falling back to ping sweep.")

    # 2) Always run ping sweep too — catches hosts that ignore ARP or are off-segment
    print("[2/2] Running ping sweep...")
    ping_results = ping_sweep(subnet)
    print(f"      Found {len(ping_results)} host(s) via ping.")

    devices = merge_results(arp_results, ping_results)
    print_table(devices)

    print(f"\nScan completed in {time.time() - start:.1f}s")

    # CSV export: `python scan.py --save results.csv`
    if '--save' in sys.argv:
        idx = sys.argv.index('--save')
        if idx + 1 < len(sys.argv):
            save_csv(devices, sys.argv[idx + 1])


if __name__ == '__main__':
    main()