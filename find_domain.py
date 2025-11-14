import os

# Test olarak direkt dosya oluştur
current_dir = os.getcwd()
file_path = os.path.join(current_dir, "working_domain.txt")
print("Mevcut dizin:", current_dir)

try:
    with open(file_path, "w") as f:
        f.write("https://justsporthd99.xyz\n")
    print("Dosya oluşturuldu!")
except Exception as e:
    print("Dosya oluşturulamadı:", e)

print("Dizin içeriği:", os.listdir(current_dir))
