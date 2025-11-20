import speedtest

# Initialize speedtest
router_check = speedtest.Speedtest()

# Declare variables for download and upload speed (bits per second) 
download_bps = router_check.download()
upload_bps = router_check.upload()

# Convert bts to mbps (1 mbps = 1,000,000)
download_mbps = round(download_bps / 1_000_000, 2)
upload_mbps = round(upload_bps / 1_000_000, 2)


# Print download and upload speed
print(f"Download Speed (Approx.): {download_mbps} Mbps")
print(f"Upload Speed: {upload_mbps} Mbps")


