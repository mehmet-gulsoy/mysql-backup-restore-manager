import subprocess
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKUP_DIR = os.path.join(BASE_DIR, "backups")


def backup_database(user, password, db_name):
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    filename = os.path.join(
        BACKUP_DIR,
        f"{db_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
    )

    command = [
        "mysqldump", "-u", user, f"-p{password}", db_name,
        "-r", filename
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        return f"✅ Yedekleme başarılı\nDosya: {filename}"
    else:
        return f"❌ Yedekleme hatası:\n{result.stderr}"
