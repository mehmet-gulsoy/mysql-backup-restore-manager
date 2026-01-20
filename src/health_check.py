import subprocess

def run_health_check():
    print("🔍 İlk sistem kontrolü yapılıyor...")

    try:
        subprocess.run(["python", "tests/self_check.py"], check=True)
        print("🎉 Sistem ilk kontrolden başarıyla geçti.")
    except:
        print("⚠️ Sistem kontrolünde hata var.")
