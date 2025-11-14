import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
HEADERS = {"User-Agent": USER_AGENT}

def check_domain(i):
    url = f"https://justsporthd{i}.xyz/"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200 and "JustSportHD" in r.text:
            print(f"✅ {url} çalışıyor!")
            return url
        else:
            print(f"❌ {url} yanıt verdi ama içerik uygun değil (status={r.status_code})")
    except Exception as e:
        print(f"❌ {url} başarısız: {e}")
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
    # GitHub Actions ortam değişkeni mutlaka olmalı
    repo_dir = os.environ.get("GITHUB_WORKSPACE")
    if not repo_dir:
        raise RuntimeError("GITHUB_WORKSPACE env değişkeni bulunamadı!")

    os.makedirs(repo_dir, exist_ok=True)
    file_path = os.path.join(repo_dir, "working_domain.txt")
    print("Dosya yazılacak dizin:", file_path)

    domain = find_working_domain_parallel()
    if not domain:
        print("⚠️ Domain bulunamadı, varsayılan domain kullanılacak")
        domain = "https://justsporthd99.xyz"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(domain + "\n")

    print("Dosya oluşturuldu:", file_path)

if __name__ == "__main__":
    main()
