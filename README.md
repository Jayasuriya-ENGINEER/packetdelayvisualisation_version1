# Packet Delay Visualization Using Wireshark Logs

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![OS](https://img.shields.io/badge/OS-Ubuntu%2022.04-green.svg)]()
[![GUI](https://img.shields.io/badge/Framework-PyQt5%20%7C%20PyQtGraph-orange.svg)]()
[![Network](https://img.shields.io/badge/Network-Scapy%20%7C%20Wireshark-yellow.svg)]()

---

## Overview

**Packet Delay Visualization Using Wireshark Logs** is a Python-based tool designed to simplify network latency and delay analysis through an interactive, user-friendly interface.

While tools like Wireshark offer detailed packet inspection, they lack simple visualizations for delay and jitter.  
This project bridges that gap by providing real-time and offline packet delay visualization using Python, Scapy, PyQt5, and PyQtGraph.

The system allows users to:
- Capture live network packets using **Scapy**
- Analyze and visualize **packet delays, jitter, and losses**
- Map packets to their originating **applications** using `psutil`
- Generate **interactive charts** through a PyQt-based GUI
- Export the analyzed data as **CSV** or **JSON**

---

## Key Features

| Feature | Description |
|----------|-------------|
| Live Packet Capture | Capture and monitor live packets from the network using Scapy |
| Offline Analysis | Analyze previously recorded `.pcap` files |
| Application Mapping | Map network ports to active applications using `psutil` |
| Real-Time Visualization | Display delay, jitter, and loss data dynamically using PyQtGraph |
| Data Export | Export analysis results as CSV or JSON for external processing |
| User-Friendly GUI | Interactive interface built using PyQt5 for better usability |

---

## Technology Stack

| Component | Technology Used |
|------------|-----------------|
| Operating System | Ubuntu 22.04 |
| Programming Language | Python 3.10 |
| Frameworks / Libraries | PyQt5, PyQtGraph, Scapy, psutil |
| Tools Used | Wireshark, Visual Studio Code |
| Visualization | Real-time charts using PyQtGraph |
| Supported File Formats | PCAP, CSV, JSON |

---

## System Workflow

1. **Packet Capture**  
   Scapy captures network packets either in real-time or from `.pcap` files.

2. **Data Processing**  
   Extracts timestamps, IP addresses, and computes delay and jitter metrics.

3. **Application Mapping**  
   Uses psutil to associate network connections with running applications.

4. **Visualization**  
   Displays delay, jitter, packet loss, and protocol distribution graphs using PyQtGraph.

5. **Data Export**  
   Enables export of summarized results in CSV or JSON format for further analysis.

---

## Team Members and Responsibilities

| Name | Role | Responsibilities |
|------|------|------------------|
| **Jaya Suriya S** | Lead Developer & Designer | Designed and implemented the GUI using PyQt5 and PyQtGraph, integrated real-time visualization modules, and handled documentation and version control. |
| **Manikandan K** | System Architect & Backend Developer | Developed core logic for packet capture and delay computation using Scapy, designed backend architecture, and ensured smooth integration between modules. |
| **Parthipan M** | Testing and Analysis Engineer | Performed testing on packet delay computation accuracy, validated visualization outputs, and analyzed sample Wireshark data sets for consistency. |
| **Keerthivarman S D** | Implementation and Deployment (platform specific) | Managed setup and deployment on Ubuntu environment, configured runtime dependencies, and handled final implementation and demonstrations. |

---

## Example Output

- **Real-Time Graphs:** Dynamic display of delay and jitter over time.  
- **Protocol Distribution:** Graphical representation of protocol usage (TCP, UDP, ICMP, etc.).  
- **Application Mapping:** Identification of applications contributing to traffic load.  
- **Exported Reports:** Structured CSV/JSON output summarizing packet-level metrics.

---

## Future Enhancements

- Integration of **machine learning** models for anomaly detection.  
- Implementation of **predictive delay analytics** for performance optimization.  
- Development of a **web-based dashboard** for remote monitoring.  
- Automated **PDF report generation** from captured data.

---

## References

1. S. Wang et al., “Analysis and Application of Wireshark in TCP/IP Protocol Teaching,” *IEEE EDT 2010*.  
2. D. Upadhyay et al., “In-depth Analysis of Email Protocols using Wireshark,” *INCOFT 2023*.  
3. J. Gomez et al., “Traffic Classification in IP Networks Through ML,” *IEEE Access 2023*.  
4. GeeksforGeeks – *Wireshark Packet Capturing and Analyzing*.  
5. Varonis – *How to Use Wireshark*.  

---

## Conclusion

This project presents an efficient and accessible solution for analyzing and visualizing packet delays in network traffic.  
By combining **Scapy** for packet handling, **PyQt5** for GUI design, and **PyQtGraph** for visualization, it delivers an integrated tool that bridges the gap between raw network data and insightful analysis.  
The tool enhances understanding of network latency, helping users monitor, troubleshoot, and optimize network performance effectively.

---

## Setup Instructions

### Prerequisites
- Python 3.10 or higher  
- Ubuntu 22.04 (recommended)  
- Wireshark installed for packet capture validation
