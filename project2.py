#!/usr/bin/env python3
# Author(s): Mehran Ebrahimi (main block), Junlong Wang (output formatting)
# Description: Main script that runs the system health checker with argparse options.

import argparse
from disk_check import get_disk_usage
from mem_check import get_memory_usage
from cpu_check import get_cpu_load

def format_output(title, data):
    print("\n" + "=" * 40)
    print(f"{title}")
    print("=" * 40)
    for key, value in data.items():
        print(f"{key:15}: {value}")
    print()

def main():
    parser = argparse.ArgumentParser(description="System Health Checker: View disk, memory, and CPU usage")
    parser.add_argument('--disk', action='store_true', help='Show disk usage')
    parser.add_argument('--mem', action='store_true', help='Show memory usage')
    parser.add_argument('--cpu', action='store_true', help='Show CPU load averages')
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        return

    if args.disk:
        disk = get_disk_usage()
        format_output("Disk Usage Report", disk)

    if args.mem:
        mem = get_memory_usage()
        format_output("Memory Usage Report", mem)

    if args.cpu:
        cpu = get_cpu_load()
        format_output("CPU Load Report", cpu)

if __name__ == '__main__':
    main()
