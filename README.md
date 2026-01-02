# Reconify 🔍  
### Lightweight Security Awareness Tool

Reconify is a beginner-friendly Python-based security awareness and reconnaissance tool.  
It helps identify basic security exposure by checking website reachability and commonly
exposed sensitive endpoints — strictly for **authorized and educational use only**.

---

## 🚀 Features
- Checks if a target URL is reachable
- Displays HTTP status code
- Assigns a basic risk level (LOW / MEDIUM / HIGH)
- Scans common sensitive endpoints:
  - `/admin`
  - `/login`
  - `/dashboard`
- Simple CLI-based interaction
- Lightweight and easy to understand for beginners

---

## 🛠️ Tech Stack
- Python 3
- `requests` library

---

## 📦 Installation

```bash
pip install requests

Reconify
Lightweight Security Awareness Tool

Target reachable
Status Code: 200
Risk Level: LOW

Checking common sensitive paths
/admin not accessible
/login not accessible
/dashboard not accessible

## ⚠️ Disclaimer
This tool is created strictly for educational purposes.  
Use it only on targets you own or have explicit permission to test.