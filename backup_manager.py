import subprocess
import datetime
import os

def take_backup():
    db_name = "test_backup"
    user = "root"
    password = "mysql123"

    
    backup_dir = os.path.join(os.path.dirname(__file__), "backups")

    
    filename = f"{db_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
    filepath = os.path.join(backup_dir, filename)

    command = f'mysqldump -u {user} -p{password} {db_name} > "{filepath}"'

    try:
        subprocess.run(command, shell=True, check=True)
        print("✅ Backup başarıyla alındı:")
        print(filepath)
    except Exception as e:
        print("❌ Backup alınırken hata oluştu:")
        print(e)


if __name__ == "__main__":
    take_backup()
