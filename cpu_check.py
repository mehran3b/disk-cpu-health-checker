#!/usr/bin/env python3
# Author(s): Urmil Rohitkumar Patel
# Description: This file contains a function to check CPU load averages using os.getloadavg()

import os

def get_cpu_load():
    try:
        load1, load5, load15 = os.getloadavg()
        return {
            "1 min avg": round(load1, 2),
            "5 min avg": round(load5, 2),
            "15 min avg": round(load15, 2)
        }
    except AttributeError:
        return {"Error": "CPU load average not supported on this system"}

if __name__ == "__main__":
    result = get_cpu_load()
    print("CPU Load Averages:")
    for key, value in result.items():
        print(f"{key}: {value}")
