import os

# Repo kök dizini
repo_dir = os.environ.get("GITHUB_WORKSPACE", os.getcwd())
file_path = os.path.join(repo_dir, "working_domain.txt")

print("Dosya yazılacak dizin:", repo_dir)
print("Mutlak dosya yolu:", file_path)

try:
    with open(file_path, "w") as f:
        f.write("https://justsporthd99.xyz\n")
    print("Dosya oluşturuldu!")
except Exception as e:
    print("Dosya oluşturulamadı:", e)

print("Dizin içeriği:", os.listdir(repo_dir))
