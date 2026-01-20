import os
import subprocess

def mysql_restore(user, password, backup_dir="backups"):
    if not os.path.exists(backup_dir):
        print("❌ Yedek klasörü bulunamadı.")
        return

    yedekler = [f for f in os.listdir(backup_dir) if f.endswith(".sql")]

    if not yedekler:
        print("❌ Geri yüklenecek yedek bulunamadı.")
        return

    print("\n=== Mevcut Yedekler ===")
    for i, dosya in enumerate(yedekler, 1):
        print(f"{i}) {dosya}")

    secim = input("Geri yüklenecek yedeğin numarasını seçin: ")

    try:
        secim = int(secim) - 1
        secilen_dosya = yedekler[secim]
    except:
        print("❌ Geçersiz seçim.")
        return

    veritabani = input("Geri yüklenecek veritabanı adı: ")
    dosya_yolu = os.path.join(backup_dir, secilen_dosya)

    komut = [
        "mysql",
        "-u", user,
        f"-p{password}",
        veritabani
    ]

    try:
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            subprocess.run(komut, stdin=dosya, stderr=subprocess.PIPE, check=True)

        print("✅ Geri yükleme başarıyla tamamlandı.")

    except subprocess.CalledProcessError as hata:
        print("❌ Geri yükleme sırasında hata oluştu:")
        print(hata.stderr.decode("utf-8"))
