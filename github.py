print('hello world')
import os
import platform
import socket
import time
import subprocess

# Hostname og OS
print("Maskinnavn:", socket.gethostname())
print("OS:", platform.system(), platform.release())

# Oppetid (Linux / Raspberry Pi)
with open("/proc/uptime") as f:
    sekunder = float(f.readline().split()[0])
    timer = int(sekunder // 3600)
    print("Oppetid:", timer, "timer")

# Temperatur (kun Raspberry Pi)
try:
    temp = subprocess.check_output(["vcgencmd", "measure_temp"]).decode()
    print("Temperatur:", temp.strip())
except Exception:
    print("Temperatur: Ikke tilgjengelig (ikke Raspberry Pi?)")
