Bu proje, açık kaynak işletim sistemleri dersi kapsamında geliştirilen bir **MySQL Backup – Restore – Config Yönetim Aracı**dır.  
Amaç, veritabanı bakım operasyonlarını otomatik ve kullanıcı dostu bir şekilde gerçekleştirebilen bir sistem geliştirmektir.

Proje Windows işletim sistemi üzerinde, Python ve MySQL kullanılarak geliştirilmiştir.

---

## 🎯 Proje Amacı

Bu projenin temel hedefleri:

- MySQL veritabanlarının otomatik olarak yedeğini almak (Backup)
- Alınan yedekleri geri yüklemek (Restore)
- MySQL yapılandırma dosyalarını (my.cnf / my.ini) düzenleyebilmek
- Sistem durumunu otomatik kontrol edebilmek (Auto Control Ability)
- Kendi fonksiyonlarını test edebilen bir yapı sunmak (Auto Test Ability)

---

## 🛠 Kullanılan Teknolojiler

- **İşletim Sistemi:** Windows 10 / 11  
- **Veritabanı:** MySQL Server 8.0  
- **Programlama Dili:** Python 3.13  
- **Arayüz:** Python Tkinter (basit ve modern tasarım)  
- **Araçlar:**  
  - mysqldump  
  - MySQL Workbench  

---

## 📂 Proje Klasör Yapısı

mysql-backup-restore-manager/
│
├─ researchs/ # AI araştırma çıktıları
├─ specs/ # Teknik gereksinimler ve analiz dokümanları
├─ src/ # Python kaynak kodları
├─ docs/ # Proje dokümantasyonu
└─ README.md # Proje tanıtım dosyası
