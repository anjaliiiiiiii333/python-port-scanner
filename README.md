# 🔒 Python Vulnerability Scanner

A simple Python-based Vulnerability Scanner developed as a mini cybersecurity project. The scanner identifies open ports, detects common network services, performs basic vulnerability checks, and generates a vulnerability report.

---

## 📌 Features

- Scan common network ports
- Detect common services (HTTP, SSH, FTP, SMB, etc.)
- Perform basic vulnerability assessment
- Attempt software version detection using banner grabbing
- Generate a vulnerability report
- Display scan time

---

## 🛠 Technologies Used

- Python 3
- Socket Programming
- Time Module
- Datetime Module

---

## 📂 Project Structure

```
vulnerability-scanner/
│── scanner.py
│── vulnerability_report.txt
│── README.md
```

---

## ▶️ How to Run

1. Clone the repository

```
git clone https://github.com/anjaliiiiiiii333/python-port-scanner
```

2. Navigate to the project folder

```
cd network-scanner
```

3. Run the scanner

```
python scanner.py
```

4. Enter the target hostname or IP address.

Example:

```
localhost
```

or

```
127.0.0.1
```

---

## 📋 Sample Output

```
Scanning Target: localhost

Port 135 OPEN (RPC)
Port 445 OPEN (SMB)

Potential Vulnerabilities:
- SMB is exposed.

Report saved successfully as vulnerability_report.txt
```

---

## 📄 Report

The scanner generates a text report containing:

- Target information
- Open ports
- Version detection attempt
- Potential vulnerabilities
- Security recommendations

---

## ⚠ Disclaimer

This tool is developed for educational purposes only. Scan only systems that you own or have permission to test.

---

## 🚀 Future Improvements

- Multi-threaded scanning
- GUI interface
- CVE database integration
- Better service version detection
- Export reports in PDF or HTML