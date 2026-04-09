import subprocess
import socket
import struct
import ipaddress
import concurrent.futures
import time
import os
from datetime import datetime
from scapy.all import *

# Return scan origins LAN IP address
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
    except socket.herror:
        return ip
    
def arp_scan(subnet):
    arp = arp(pdst=subnet)
    ether = ether(dst="ff:ff:ff:ff:ff:ff")
    answered, _ = srp(ether / arp, timeout=2, verbose=False)

    devices = []
    for _, rcv in answered:
        ip = rcv[arp].psrc
        mac = rcv[ether].src   
        devices.append({'ip': ip, 'mac': mac, 'hostname': resolve_hostname(ip)})
    return devices


"""
Pings a single device and returns IP if host is alive
"""
def ping_host(ip):
    cmd = ['ping', '-n', '1', '-w', '500', str(ip)]
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return str(ip)

"""
Pull MAC for ip from the OS ARP cache after a successful ping 
"""
def get_mac_from_arp_table(ip):
    try:
        out = subprocess.check_output(['arp', '-a', ip], stderr=subprocess.DEVNULL, text=True)
        for line in out.splitlines():
            parts = line.split()
            if len(parts) >= 2 and ip in parts[0]:
                return parts[1].replace('-', ':').lower()
    except subprocess.CalledProcessError:
        pass 
    return 'unknown'

"""
Fallback ping sweep + ARP lookup in case the first scans fail or return null values
"""
def ping_sweep(subnet):
    hosts = list(ipaddress.IPv4Network(subnet, strict=False).hosts())

    print(f" Pinging {len(hosts)} hosts in parallel...")
    alive = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=64) as pool:
        for ip in pool.map(ping_host,hosts):
            if ip:
                alive.append(ip)

    devices = []
    for ip in sorted (alive, key=lambda x: ipaddress.IPv4Address(x)):
        mac = get_mac_from_arp_table(ip)
        hostname = resolve_hostname(ip)
        devices.append({'ip': ip, 'mac': mac, 'hostname': hostname})
    return devices