import tkinter as tk
from tkinter import ttk, simpledialog
import threading

import health_check
import self_test
import backup
import restore


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("MySQL Backup & Restore Manager")
        self.root.geometry("700x450")
        self.root.configure(bg="#2c2f33")

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root,
                         text="MySQL Backup & Restore Manager",
                         font=("Segoe UI", 18, "bold"),
                         bg="#2c2f33",
                         fg="white")
        title.pack(pady=15)

        frame = tk.Frame(self.root, bg="#2c2f33")
        frame.pack(pady=10)

        ttk.Button(frame, text="🔍 Sistem Kontrolü", width=25,
                   command=self.run_health_check).grid(row=0, column=0, padx=10, pady=8)

        ttk.Button(frame, text="🧪 Self Test", width=25,
                   command=self.run_self_test).grid(row=0, column=1, padx=10, pady=8)

        ttk.Button(frame, text="💾 Yedek Al", width=25,
                   command=self.run_backup).grid(row=1, column=0, padx=10, pady=8)

        ttk.Button(frame, text="♻️ Geri Yükle", width=25,
                   command=self.run_restore).grid(row=1, column=1, padx=10, pady=8)

        ttk.Button(frame, text="⚙️ Çıkış", width=25,
                   command=self.root.quit).grid(row=2, column=0, columnspan=2, pady=12)

        self.log = tk.Text(self.root, height=10, bg="#23272a", fg="white", font=("Consolas", 10))
        self.log.pack(fill="both", padx=15, pady=10)

    def write_log(self, text):
        self.log.insert(tk.END, text + "\n")
        self.log.see(tk.END)

    def ask_input(self, title):
        return simpledialog.askstring("Bilgi Girişi", title)

    def run_health_check(self):
        self.log.delete(1.0, tk.END)

        def task():
            self.write_log("Sistem kontrolü başlatılıyor...\n")
            ok = health_check.run_health_check()
            if ok:
                self.write_log("\nSONUÇ: Sistem hazır ✅")
            else:
                self.write_log("\nSONUÇ: Sistem hazır değil ❌")

        threading.Thread(target=task).start()

    def run_self_test(self):
        self.log.delete(1.0, tk.END)

        def task():
            user = self.ask_input("MySQL kullanıcı adı")
            password = self.ask_input("MySQL şifre")

            self.write_log("Self test başlatılıyor...\n")
            self_test.self_test(user, password)

        threading.Thread(target=task).start()

    def run_backup(self):
        self.log.delete(1.0, tk.END)

        def task():
            user = self.ask_input("MySQL kullanıcı adı")
            password = self.ask_input("MySQL şifre")
            db = self.ask_input("Veritabanı adı")

            result = backup.backup_database(user, password, db)
            self.write_log(result)

        threading.Thread(target=task).start()

    def run_restore(self):
        self.log.delete(1.0, tk.END)

        def task():
            user = self.ask_input("MySQL kullanıcı adı")
            password = self.ask_input("MySQL şifre")
            db = self.ask_input("Veritabanı adı")
            file = self.ask_input("Yedek dosya yolu")

            result = restore.restore_database(user, password, db, file)
            self.write_log(result)

        threading.Thread(target=task).start()
