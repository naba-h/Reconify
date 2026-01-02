import requests

print("=" * 50)
print("Reconify")
print("Lightweight Security Awareness Tool")
print("=" * 50)

target = input("Enter target URL (authorized only): ").strip()

try:
    response = requests.get(target, timeout=5)
    print("\n[+] Target reachable")
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("Risk Level: LOW")
    elif response.status_code in [301, 302]:
        print("Risk Level: MEDIUM")
    else:
        print("Risk Level: HIGH")

except Exception:
    print("\n[-] Target not reachable")
    print("Risk Level: HIGH")
    exit()

# Basic sensitive endpoint checks
print("\n[+] Checking common sensitive paths")

sensitive_paths = ["/admin", "/login", "/dashboard"]

for path in sensitive_paths:
    try:
        url = target.rstrip("/") + path
        r = requests.get(url, timeout=5)

        if r.status_code == 200:
            print(f"[!] {path} accessible (Risk: MEDIUM)")
        elif r.status_code in [401, 403]:
            print(f"[-] {path} protected")
        else:
            print(f"[-] {path} not accessible")

    except:
        print(f"[!] Error checking {path}")