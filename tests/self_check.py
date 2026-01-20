import subprocess


def check_mysql_service():
    print("MySQL servisi kontrol ediliyor...")
    try:
        result = subprocess.run(["sc", "query", "MySQL80"], capture_output=True, text=True)
        if "RUNNING" in result.stdout:
            print("✅ MySQL servisi çalışıyor.")
        else:
            print("❌ MySQL servisi çalışmıyor.")
    except:
        print("❌ MySQL servisi kontrol edilemedi.")


def check_mysqldump():
    print("mysqldump kontrol ediliyor...")
    try:
        subprocess.run(["mysqldump", "--version"], check=True, stdout=subprocess.DEVNULL)
        print("✅ mysqldump kullanılabilir.")
    except:
        print("❌ mysqldump bulunamadı (PATH sorunu olabilir).")


def check_python():
    print("Python kontrol ediliyor...")
    try:
        subprocess.run(["python", "--version"], check=True)
        print("✅ Python çalışıyor.")
    except:
        print("❌ Python çalışmıyor.")


if __name__ == "__main__":
    print("=== Sistem Self-Check Başladı ===\n")

    check_mysql_service()
    check_mysqldump()
    check_python()

    print("\n=== Sistem Self-Check Bitti ===")
