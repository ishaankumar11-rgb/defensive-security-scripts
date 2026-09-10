
# Defensive Security Scripts 🛡️

A collection of secure, legal, and educational Python scripts designed for network auditing, baseline vulnerability assessments, and defensive security workflows.

## 🚀 Included Tools

### 1. Simple Port Scanner (`port_scanner.py`)
A python script utilizing native sockets to scan open ports on local network configurations.

* **Target Host:** Configured to `127.0.0.1` (Localhost) for secure loopback auditing.
* **Ports Audited:** Standard infrastructure ports including 21 (FTP), 22 (SSH), 80 (HTTP), 443 (HTTPS), and 8080.
### 2. File Integrity Monitor (`file_monitor.py`)
A continuous validation script utilizing the SHA-256 hashing algorithm to monitor critical file loops for unauthorized changes.

* **Automation:** Scans target parameters at a configurable interval (Default: 5 seconds).
* **Alert System:** Generates immediate timestamped logs if the hash deviates from the established secure baseline.

---
## 📦 Installation & Terminal Usage

Open your Linux/Mac/Termux terminal and run the following commands to clone and install the tools globally:

```bash
# 1. Clone the repository
git clone https://github.com

# 2. Navigate into the directory
cd defensive-security-scripts

# 3. Install the tools locally
pip install -e .
```

### 🛠️ How to Run Directly from Terminal:
Once installed, you can trigger the scripts from **any directory** in your terminal using these shortcut commands:

* To run the Port Scanner:
  ```bash
  sec-scan
  ```
* To run the File Integrity Monitor:
  ```bash
  sec-monitor
  ```

## ⚖️ Disclaimer & Educational Purpose

This repository is maintained strictly for **educational, compliance, and defensive purposes**. The utilities contained herein are intended to assist developers and security administrators in auditing their own local systems and authorized network loops. 

**Unauthorized usage or scanning against third-party assets without explicit prior consent is strictly prohibited.**
