import subprocess
import os

def check_mysql_service():
    try:
        result = subprocess.run("mysql --version", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ MySQL yüklü ve erişilebilir")
            return True
        else:
            print("❌ MySQL bulunamadı")
            return False
    except:
        print("❌ MySQL kontrol edilirken hata oluştu")
        return False


def check_backup_folder():
    backup_dir = os.path.join(os.path.dirname(__file__), "..", "backups")

    if os.path.exists(backup_dir):
        print("✅ Backup klasörü mevcut")
        return True
    else:
        print("❌ Backup klasörü bulunamadı")
        return False


def check_backup_files():
    backup_dir = os.path.join(os.path.dirname(__file__), "..", "backups")

    files = [f for f in os.listdir(backup_dir) if f.endswith(".sql")]

    if files:
        print(f"✅ {len(files)} adet backup dosyası bulundu")
        return True
    else:
        print("❌ Hiç backup dosyası bulunamadı")
        return False


def run_self_check():
    print("🔍 Sistem Kontrolü Başlatıldı...\n")

    mysql_ok = check_mysql_service()
    folder_ok = check_backup_folder()
    files_ok = check_backup_files()

    print("\n📊 Sonuç:")

    if mysql_ok and folder_ok and files_ok:
        print("🎉 SİSTEM HAZIR — TÜM KONTROLLER BAŞARILI")
    else:
        print("⚠️ SİSTEMDE EKSİKLER VAR — LÜTFEN KONTROL EDİN")


if __name__ == "__main__":
    run_self_check()
