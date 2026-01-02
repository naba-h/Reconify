import requests

print("=" * 40)
print(" Reconify ")
print(" Lightweight Security Awareness Tool ")
print("=" * 40)

target = input("Enter target URL (authorized only): ")

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

except Exception as e:
    print("\n[-] Target not reachable")
    print("Risk Level: HIGH")
    print("\n[+] Checking common sensitive paths (basic check)")

sensitive_paths = ["/admin", "/login", "/dashboard"]

for path in sensitive_paths:
    try:
        url = target.rstrip("/") + path
        r = requests.get(url, timeout=5)

        if r.status_code == 200:
            print(f"[!] Accessible endpoint found: {path} (Risk: MEDIUM)")
        elif r.status_code in [401, 403]:
            print(f"[-] Protected endpoint: {path} (Good)")
        else:
            print(f"[-] {path} not accessible")

    except:
        print(f"[!] Error checking {path}")

