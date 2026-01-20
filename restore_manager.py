import subprocess
import os

def restore_backup():
    user = "root"
    password = "mysql123"
    restore_db = "test_restore"

    backup_dir = os.path.join(os.path.dirname(__file__), "backups")

    # klasördeki ilk .sql dosyasını al (istersen sonuncuyu da seçebiliriz)
    files = [f for f in os.listdir(backup_dir) if f.endswith(".sql")]

    if not files:
        print("❌ Restore edilecek backup bulunamadı.")
        return

    backup_file = files[-1]  # en son alınan

    filepath = os.path.join(backup_dir, backup_file)

    command = f'mysql -u {user} -p{password} {restore_db} < "{filepath}"'

    try:
        subprocess.run(command, shell=True, check=True)
        print("✅ Restore başarıyla tamamlandı:")
        print(filepath)
    except Exception as e:
        print("❌ Restore sırasında hata oluştu:")
        print(e)


if __name__ == "__main__":
    restore_backup()
