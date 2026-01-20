import tkinter as tk
import gui
import health_check


def main():
    print("=== MySQL Backup & Restore Manager ===")
    print("Sistem ilk kontrolü yapılıyor...\n")

    health_check.run_health_check()

    print("\nArayüz başlatılıyor...")

    root = tk.Tk()
    app = gui.App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
