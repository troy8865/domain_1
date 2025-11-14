import os
import requests

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
HEADERS = {"User-Agent": USER_AGENT}

def check_domain(i):
    url = f"https://justsporthd{i}.xyz/"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200 and "JustSportHD" in r.text:
            return url
    except:
        pass
    return None

def main():
    repo_dir = os.environ.get("GITHUB_WORKSPACE", ".")
    file_path = os.path.join(repo_dir, "working_domain.txt")

    working_domain = None
    for i in range(40, 101):
        domain = check_domain(i)
        if domain:
            working_domain = domain
            break

    if not working_domain:
        working_domain = "https://justsporthd99.xyz"  # fallback

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(working_domain + "\n")

    print(f"Dosya oluşturuldu: {file_path}")
    print(f"Çalışan domain: {working_domain}")

if __name__ == "__main__":
    main()
