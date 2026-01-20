# MySQL Backup & Restore Manager

Bu proje, Windows işletim sistemi üzerinde çalışan MySQL veritabanları için  
**otomatik yedek alma (backup)**, **geri yükleme (restore)** ve  
**sistem sağlık kontrolü (self-check)** işlemlerini gerçekleştiren,  
Python tabanlı ve grafik arayüzlü bir yönetim aracıdır.

Proje, Açık Kaynak İşletim Sistemleri dersi kapsamında geliştirilmiştir.

---

## 🎯 Proje Amacı

Veritabanı bakım operasyonlarını kolaylaştırmak ve otomatik hale getirmek:

- Zamanlanabilir / manuel MySQL yedeği almak  
- Alınan yedekleri geri yüklemek  
- Sistem durumunu otomatik kontrol etmek (Auto Control)  
- Kendi test mekanizmasını çalıştırmak (Auto Test / Self-Check)  

---

## ⚙️ Kullanılan Teknolojiler

- İşletim Sistemi: Windows 10 / 11  
- Programlama Dili: Python 3.x  
- Veritabanı: MySQL 8.0  
- Arayüz: Tkinter (Python GUI)  

---

## 📁 Proje Klasör Yapısı

mysql-backup-restore-manager/
│
├── researchs/ # AI araştırma çıktıları
├── specs/ # Gereksinimler ve analiz
├── src/ # Kaynak kodlar
│ ├── backups/ # Alınan .sql yedek dosyaları
│ ├── tests/ # Self-check test dosyaları
│ │ └── self_check.py
│ ├── main.py
│ ├── gui.py
│ ├── backup_manager.py
│ ├── restore_manager.py
│ └── health_check.py
│
├── docs/ # Dokümantasyon ve tasarım
│ └── design.md
│
└── README.md
