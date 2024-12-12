# shebang
#!/usr/bin/env python3

import shutil
import psutil

#Create Disk Check function
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

#Create CPU Check function
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

#Create main function, and print lines
if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is OK!")