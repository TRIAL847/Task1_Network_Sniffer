# Task1_Network_Sniffer
This Is A Project Of Network Sniffer
# Task 1: Basic Network Sniffer

A lightweight Python packet sniffer built with Scapy to capture and inspect real-time IPv4 packet metadata. This tool is intended strictly for educational purposes and monitoring authorized network interfaces.

---

## Features
- Captures incoming and outgoing IPv4 traffic in real time.
- Identifies protocols: **TCP**, **UDP**, and **ICMP**.
- Displays packet metadata: timestamps, source/destination IP addresses, port pairs, and packet lengths.
- Streams live data without loading packets into memory (`store=False`).
- Does **not** inspect or log sensitive payload data.

---

## Prerequisites
- **Python 3.8+**
- **Npcap** (Windows users only): Ensure Npcap is installed with WinPcap API-compatible mode enabled.
- **Root/Administrator privileges**: Packet sniffing requires elevated socket permissions.

---

## Installation

1. Clone or extract the project files into your working directory:
   ```bash
   cd Task1_Network_Sniffer
