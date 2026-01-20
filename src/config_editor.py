import shutil

CONFIG_PATH = "my.cnf"   # Gerçekte: C:/ProgramData/MySQL/MySQL Server 8.0/my.ini

def config_menu():
    print("\n=== MySQL Yapılandırma Dosyası Düzenleyici ===")
    print("1) max_connections ayarla")
    print("2) Dosyayı yedekle")
    print("3) Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        parametre_guncelle("max_connections")

    elif secim == "2":
        dosya_yedekle()

    elif secim == "3":
        return

    else:
        print("Geçersiz seçim.")


def parametre_guncelle(parametre):
    try:
        with open(CONFIG_PATH, "r") as dosya:
            satirlar = dosya.readlines()

        yeni_deger = input(f"{parametre} için yeni değer: ")

        with open(CONFIG_PATH, "w") as dosya:
            for satir in satirlar:
                if satir.strip().startswith(parametre):
                    dosya.write(f"{parametre} = {yeni_deger}\n")
                else:
                    dosya.write(satir)

        print(f"✅ {parametre} başarıyla güncellendi.")

    except FileNotFoundError:
        print("❌ Yapılandırma dosyası bulunamadı.")


def dosya_yedekle():
    try:
        shutil.copy(CONFIG_PATH, CONFIG_PATH + ".bak")
        print("✅ Yapılandırma dosyası yedeklendi.")
    except:
        print("❌ Dosya yedekleme başarısız.")
