import subprocess
import os

TEST_DB = "test_automation_db"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKUP_DIR = os.path.join(BASE_DIR, "tests", "test_backups")
BACKUP_FILE = os.path.join(BACKUP_DIR, "test_backup.sql")


def run_command(command, shell=False):
    result = subprocess.run(command, capture_output=True, text=True, shell=shell)
    return result.returncode == 0, result.stdout + result.stderr


def self_test(user, password):
    print("\n=== SELF TEST (AUTO TEST MEKANİZMASI) ===\n")

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    # 1. Test veritabanı oluştur
    print("1) Test veritabanı oluşturuluyor...")
    ok, out = run_command([
        "mysql", "-u", user, f"-p{password}",
        "-e", f"CREATE DATABASE {TEST_DB};"
    ])
    if not ok:
        print("❌ Test veritabanı oluşturulamadı")
        print(out)
        return
    print("✅ Test veritabanı oluşturuldu")

    # 2. Test tablosu ve veri ekle
    print("2) Test tablosu ve veri ekleniyor...")
    sql_commands = f"""
    USE {TEST_DB};
    CREATE TABLE test_table (id INT PRIMARY KEY, name VARCHAR(50));
    INSERT INTO test_table VALUES (1, 'Deneme Veri');
    """
    ok, out = run_command([
        "mysql", "-u", user, f"-p{password}", "-e", sql_commands
    ])
    if not ok:
        print("❌ Test verisi eklenemedi")
        print(out)
        return
    print("✅ Test verisi eklendi")

    # 3. Yedek al
    print("3) Test veritabanı yedekleniyor...")
    ok, out = run_command([
        "mysqldump", "-u", user, f"-p{password}", TEST_DB,
        "-r", BACKUP_FILE
    ])
    if not ok:
        print("❌ Yedek alma başarısız")
        print(out)
        return
    print("✅ Yedek alındı")

    # 4. Veritabanını sil
    print("4) Test veritabanı siliniyor...")
    ok, out = run_command([
        "mysql", "-u", user, f"-p{password}",
        "-e", f"DROP DATABASE {TEST_DB};"
    ])
    if not ok:
        print("❌ Test veritabanı silinemedi")
        print(out)
        return
    print("✅ Test veritabanı silindi")

    # 5. Geri yükle (Windows shell ile)
    print("5) Yedekten geri yükleme yapılıyor...")
    run_command([
        "mysql", "-u", user, f"-p{password}",
        "-e", f"CREATE DATABASE {TEST_DB};"
    ])

    restore_cmd = f'mysql -u {user} -p{password} {TEST_DB} < "{BACKUP_FILE}"'
    ok, out = run_command(restore_cmd, shell=True)

    if not ok:
        print("❌ Geri yükleme başarısız")
        print(out)
        return

    print("✅ Geri yükleme tamamlandı")

    # 6. Veri doğrulama
    print("6) Veri doğrulanıyor...")
    ok, out = run_command([
        "mysql", "-u", user, f"-p{password}", TEST_DB,
        "-e", "SELECT * FROM test_table;"
    ])

    if "Deneme Veri" in out:
        print("\n--- SELF TEST SONUCU ---")
        print("Tüm adımlar başarıyla tamamlandı 🎉")
        print("SONUÇ: SELF TEST BAŞARILI ✅")
    else:
        print("❌ Veri doğrulanamadı")
        print("SONUÇ: SELF TEST BAŞARISIZ ❌")
