import subprocess
import sys
import shutil

def check_python():
    try:
        version = sys.version.split()[0]
        return True, f"Python bulundu (Sürüm: {version})"
    except:
        return False, "Python bulunamadı"


def check_mysql():
    try:
        result = subprocess.run(["mysql", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            return True, "MySQL istemcisi bulundu"
        else:
            return False, "MySQL istemcisi bulunamadı"
    except FileNotFoundError:
        return False, "MySQL kurulu değil veya PATH'e ekli değil"


def check_mysqldump():
    path = shutil.which("mysqldump")
    if path:
        return True, "mysqldump aracı bulundu"
    else:
        return False, "mysqldump bulunamadı (PATH ayarını kontrol edin)"


def check_mysql_service():
    try:
        result = subprocess.run(["sc", "query", "MySQL"], capture_output=True, text=True)
        if "RUNNING" in result.stdout:
            return True, "MySQL servisi çalışıyor"
        else:
            return False, "MySQL servisi çalışmıyor"
    except:
        return False, "MySQL servisi kontrol edilemedi"


def run_health_check():
    print("\n=== SİSTEM DURUM KONTROLÜ (AUTO CONTROL) ===\n")

    checks = [
        ("Python Kontrolü", check_python),
        ("MySQL Kontrolü", check_mysql),
        ("mysqldump Kontrolü", check_mysqldump),
        ("MySQL Servis Kontrolü", check_mysql_service)
    ]

    all_ok = True

    for name, func in checks:
        status, message = func()
        if status:
            print(f"[OK] {name}: {message}")
        else:
            print(f"[HATA] {name}: {message}")
            all_ok = False

    print("\n--- SONUÇ ---")
    if all_ok:
        print("✅ Sistem hazır. Tüm kontroller başarılı.")
    else:
        print("❌ Sistem hazır değil. Lütfen hataları gideriniz.")

    return all_ok


if __name__ == "__main__":
    run_health_check()
