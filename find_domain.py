import os
import requests

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
HEADERS = {"User-Agent": USER_AGENT}

# Kontrol edilecek domain aralığı
START = 40
END = 101

def check_domain(i):
    url = f"https://justsporthd{i}.xyz/"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200 and "JustSportHD" in r.text:
            return url
    except requests.RequestException:
        pass
    return None

def main():
    # Çalışma dizini (script’in olduğu dizin)
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(repo_dir, "working_domain.txt")

    working_domains = []

    print(f"🔎 Domain kontrolü başlıyor: justsporthd{START} → justsporthd{END}")

    for i in range(START, END):
        domain = check_domain(i)
        if domain:
            print(f"✅ Çalışan domain bulundu: {domain}")
            working_domains.append(domain)
        else:
            print(f"❌ justsporthd{i}.xyz başarısız")

    if not working_domains:
        print("⚠️ Hiç çalışan domain bulunamadı. Fallback domain kullanılacak.")
        working_domains.append("https://justsporthd99.xyz")

    # Dosyaya yaz
    with open(file_path, "w", encoding="utf-8") as f:
        for domain in working_domains:
            f.write(domain + "\n")

    print(f"💾 Dosya oluşturuldu: {file_path}")
    print(f"📄 İçerik:\n" + "\n".join(working_domains))

if __name__ == "__main__":
    main()
