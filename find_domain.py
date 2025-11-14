import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
HEADERS = {"User-Agent": USER_AGENT}

# Domain kontrol fonksiyonu
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

# Paralel domain taraması
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

    # Gerçek domain taraması
    domain = find_working_domain_parallel()

    # Eğer domain bulunamazsa test için sahte domain oluştur
    if not domain:
        print("⚠️ Gerçek domain bulunamadı, sahte domain kullanılacak")
        domain = "https://justsporthd99.xyz"

    # Dosya oluşturma
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, "working_domain.txt")
    print(f"Dosya yazılacak: {file_path}")

    with open(file_path, "w") as f:
        f.write(domain)

    # Workflow için env değişkeni
    github_env = os.environ.get("GITHUB_ENV")
    if github_env:
        with open(github_env, "a") as env_file:
            env_file.write("DOMAIN_FOUND=true\n")
            env_file.write(f"DOMAIN_URL={domain}\n")

    # Debug: dizin ve içerik
    print("Mevcut dizin:", current_dir)
    print("Dizin içeriği:", os.listdir(current_dir))

if __name__ == "__main__":
    main()
