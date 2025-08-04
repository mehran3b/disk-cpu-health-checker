#!/usr/bin/env python3
# Author(s): Md Taki Yasir Faraji Sadik
# Description: This file contains a function to check disk usage on the system using standard Python libraries.

import shutil

def get_disk_usage():
    usage = shutil.disk_usage("/")
    total_gb = round(usage.total / (1024 ** 3), 2)
    used_gb = round(usage.used / (1024 ** 3), 2)
    free_gb = round(usage.free / (1024 ** 3), 2)
    percent_used = round((usage.used / usage.total) * 100, 1)

    return {
        "Total (GB)": total_gb,
        "Used (GB)": used_gb,
        "Free (GB)": free_gb,
        "Usage (%)": percent_used
    }

if __name__ == "__main__":
    result = get_disk_usage()
    print("Disk Usage Information:")
    for key, value in result.items():
        print(f"{key}: {value}")
