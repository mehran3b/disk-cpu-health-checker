#!/usr/bin/env python3
# Author(s): Rojina Bhandari
# Description: This file contains a function to check memory (RAM) usage by using the `free` Linux command.

import os

def get_memory_usage():
    try:
        stream = os.popen('free -m')
        output = stream.read()
        lines = output.splitlines()

        for line in lines:
            if line.startswith("Mem:"):
                parts = line.split()
                total = int(parts[1])
                used = int(parts[2])
                free = int(parts[3])
                return {
                    "Total (MB)": total,
                    "Used (MB)": used,
                    "Free (MB)": free
                }
        return {"Error": "Unable to find memory stats in `free` output"}
    except Exception as e:
        return {"Error": str(e)}

if __name__ == "__main__":
    result = get_memory_usage()
    print("Memory Usage Information:")
    for key, value in result.items():
        print(f"{key}: {value}")
