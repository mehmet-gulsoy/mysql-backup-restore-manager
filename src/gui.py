import tkinter as tk
from tkinter import messagebox
import subprocess


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("MySQL Backup & Restore Manager")
        self.root.geometry("400x300")
        self.root.configure(bg="#2c3e50")

        title = tk.Label(
            root,
            text="MySQL Backup & Restore Manager",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#2c3e50"
        )
        title.pack(pady=20)

        btn_backup = tk.Button(
            root,
            text="📦 Backup Al",
            width=20,
            height=2,
            bg="#27ae60",
            fg="white",
            font=("Arial", 12),
            command=self.run_backup
        )
        btn_backup.pack(pady=10)

        btn_restore = tk.Button(
            root,
            text="♻️ Restore Et",
            width=20,
            height=2,
            bg="#2980b9",
            fg="white",
            font=("Arial", 12),
            command=self.run_restore
        )
        btn_restore.pack(pady=10)

        btn_check = tk.Button(
            root,
            text="🔍 Sistem Kontrol",
            width=20,
            height=2,
            bg="#f39c12",
            fg="white",
            font=("Arial", 12),
            command=self.run_self_check
        )
        btn_check.pack(pady=10)

    def run_backup(self):
        try:
            subprocess.run(["python", "backup_manager.py"], check=True)
            messagebox.showinfo("Başarılı", "Backup başarıyla alındı.")
        except:
            messagebox.showerror("Hata", "Backup alınırken hata oluştu.")

    def run_restore(self):
        try:
            subprocess.run(["python", "restore_manager.py"], check=True)
            messagebox.showinfo("Başarılı", "Restore başarıyla tamamlandı.")
        except:
            messagebox.showerror("Hata", "Restore sırasında hata oluştu.")

    def run_self_check(self):
        try:
            subprocess.run(["python", "tests/self_check.py"], check=True)
            messagebox.showinfo("Bilgi", "Sistem kontrolü tamamlandı.\nDetaylar konsolda.")
        except:
            messagebox.showerror("Hata", "Sistem kontrolü çalıştırılamadı.")
