# 🛠️ Disk and CPU Health Checker

A simple and flexible Python script to monitor disk space, memory usage, and CPU load on Linux systems. Built as part of the OPS445 course at Seneca Polytechnic.

## 🎯 Project Goal

To automate system health checks using built-in Linux commands and Python, allowing CLI-based reporting of disk, CPU, and memory stats with argparse-driven flexibility.

## 🚀 Features

- 📂 Disk usage monitoring (`df`)
- 🧠 Memory usage summary (`free`)
- 🔁 CPU load check (`uptime`)
- 🎛️ CLI flags (`--disk`, `--cpu`, `--mem`, `--all`)
- 🔒 Input validation and error handling
- 🧩 Modular design (reusable functions)

## 🛠️ Tools & Technologies

| Tool           | Purpose                      |
|----------------|------------------------------|
| Python 3       | Script logic                 |
| Ubuntu Linux   | Runtime environment          |
| Git & GitHub   | Version control              |
| Bash Terminal  | System commands              |
| Argparse       | CLI argument parsing         |

## 📦 Usage

```bash
python3 healthcheck.py --disk     # Check disk usage
python3 healthcheck.py --cpu      # Check CPU load
python3 healthcheck.py --mem      # Check memory usage
python3 healthcheck.py --all      # Check all metrics
