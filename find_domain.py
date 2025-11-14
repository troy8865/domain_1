import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
HEADERS = {"User-Agent": USER_AGENT}

def check_domain(i):
    url = f"https://justsporthd{i}.xyz/"
    try:
        r = requests.get(url, headers=HEADERS, timeout=5)
        if r.status_code == 200 and "JustSportHD" in r.text:
            return url
    except:
        pass
    return None

def find_working_domain_parallel(start=40, end=100, max_workers=10):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(check_domain, i) for i in range(start, end + 1)]
        for future in as_completed(futures):
            result = future.result()
            if result:
                return result
    return None

def main():
    auto_mode = os.environ.get("AUTO_DOMAIN_CHECK", "0") == "1"
    if not auto_mode:
        input("Domain taramasını başlatmak için Enter'a basın...")

    domain = find_working_domain_parallel()
    if domain:
        print("Çalışan domain bulundu:", domain)
        with open("working_domain.txt", "w") as f:
            f.write(domain)
        # Workflow için env değişkeni olarak kaydet
        print("DOMAIN_FOUND=true")
        with open(os.environ["GITHUB_ENV"], "a") as env:
            env.write("DOMAIN_FOUND=true\n")
    else:
        print("Domain bulunamadı.")
        with open(os.environ["GITHUB_ENV"], "a") as env:
            env.write("DOMAIN_FOUND=false\n")

if __name__ == "__main__":
    main()
