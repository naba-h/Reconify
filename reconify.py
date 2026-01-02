import requests

def normalize_target(target):
    if target.startswith("http://") or target.startswith("https://"):
        return target
    return "http://" + target

def check_target(target):
    print("\n[+] Target Analysis Started")
    print("-" * 40)

    target_url = normalize_target(target)

    try:
        response = requests.get(target_url, timeout=5)
        status = response.status_code

        print(f"[+] Target Reachable: YES")
        print(f"[+] HTTP Status Code: {status}")

        if status in [200, 401, 403]:
            risk = "LOW"
        else:
            risk = "MEDIUM"

        print(f"[+] Initial Risk Level: {risk}")

        print("\n[+] Explanation:")
        print("The HTTP status code shows how the server responds.")
        print("Protected or inaccessible endpoints reduce security risks.")

    except Exception as e:
        print("[!] Target not reachable")
        print("Reason:", e)
        return

    print("\n[+] Checking common sensitive paths")
    print("-" * 40)

    sensitive_paths = {
        "/admin": "Admin panels should never be publicly accessible.",
        "/login": "Login pages can be targeted for brute-force attacks.",
        "/dashboard": "Dashboards may expose sensitive user data."
    }

    findings = 0

    for path, explanation in sensitive_paths.items():
        try:
            url = target_url.rstrip("/") + path
            r = requests.get(url, timeout=5)

            if r.status_code == 200:
                findings += 1
                print(f"[!] Accessible: {path}")
                print(f"    Why it matters: {explanation}")
                print("    Impact: Increased risk of unauthorized access\n")
            elif r.status_code in [401, 403]:
                print(f"[+] Protected: {path} (Good security practice)\n")
            else:
                print(f"[-] Not accessible: {path}\n")

        except:
            print(f"[!] Error checking {path}\n")

    print("\n[+] Final Summary")
    print("-" * 40)

    if findings == 0:
        print("✔ No common sensitive endpoints exposed.")
        print("✔ Overall Risk Assessment: LOW")
    else:
        print(f"⚠ {findings} potentially sensitive endpoints found.")
        print("⚠ Overall Risk Assessment: MEDIUM")

    print("\n[+] Note:")
    print("This analysis is for educational and authorized testing only.")


if __name__ == "__main__":
    target = input("Enter target (example.com or https://example.com): ").strip()
    check_target(target)