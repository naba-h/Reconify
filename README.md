# Reconify 🔍

**Reconify** is a beginner-friendly, Python-based **Security Awareness & Reconnaissance Tool**.  
It helps users understand basic website exposure by checking reachability, HTTP response behavior, and the accessibility of common sensitive paths — **strictly for educational and authorized use only**.

---

## 🚀 Features

- Accepts both domain names and full URLs (`example.com`, `http://`, `https://`)
- Automatically normalizes the target URL
- Checks if a target website is reachable
- Displays HTTP status codes with simple explanations
- Assesses a basic risk level (LOW / MEDIUM)
- Scans common sensitive paths:
  - `/admin`
  - `/login`
  - `/dashboard`
- Provides **educational explanations** for why exposed paths matter
- Designed for beginners learning cybersecurity concepts

---

## 🛠️ Requirements

- Python **3.8 or higher**
- `requests` library

Install dependency:
```bash
pip install requests

```
### 🧪 Sample Input

You can provide the target in any of the following formats:

```text
example.com
https://example.com
http://example.com

---

### 📊 Sample Output
```text
[+] Target Reachable: YES
[+] HTTP Status Code: 200
[+] Initial Risk Level: LOW

/admin     → Not accessible
/login     → Not accessible
/dashboard → Not accessible

✔ Overall Risk Assessment: LOW

---

## ⚠️ Disclaimer

This tool is created **strictly for educational purposes**.

Use it **only on targets you own** or where you have **explicit permission** to test.

The author is **not responsible** for any misuse of this tool.