# Sistem Tasarımı ve Mimari Dokümanı

## 1. Giriş

Bu doküman, “MySQL Veritabanı Yedekleme, Geri Yükleme ve Yapılandırma Aracı” projesinin genel mimarisini, bileşenlerini ve çalışma prensibini açıklamaktadır.

Proje, MySQL veritabanı bakım işlemlerini otomatikleştirmek amacıyla Python programlama dili kullanılarak geliştirilmiştir.

---

## 2. Genel Mimari

Sistem, modüler bir yapı üzerine kurulmuştur. Her bir bakım operasyonu ayrı bir Python modülü tarafından yönetilmektedir.

Ana bileşenler:

- Ana Menü Modülü (main.py)  
- Yedekleme Modülü (backup.py)  
- Geri Yükleme Modülü (restore.py)  
- Yapılandırma Yönetim Modülü (config_editor.py)  

Kullanıcı, ana menü üzerinden ilgili modülleri çağırarak işlemlerini gerçekleştirmektedir.

---

## 3. Bileşenler

### 3.1 Ana Menü Modülü (main.py)

Bu modül, kullanıcı ile etkileşimi sağlar.

Görevleri:
- Menü arayüzünü oluşturmak  
- Kullanıcı seçimlerine göre ilgili modülleri çağırmak  
- Program akışını yönetmek  

---

### 3.2 Yedekleme Modülü (backup.py)

Bu modül MySQL veritabanı yedekleme işlemini gerçekleştirir.

İşlevleri:
- Kullanıcıdan veritabanı bilgilerini almak  
- mysqldump komutunu çalıştırmak  
- Zaman damgalı yedek dosyası oluşturmak  
- Hata durumlarını kullanıcıya bildirmek  

---

### 3.3 Geri Yükleme Modülü (restore.py)

Bu modül mevcut yedek dosyalarından geri yükleme işlemi yapar.

İşlevleri:
- Yedek klasörünü taramak  
- Mevcut yedekleri listelemek  
- Kullanıcı tarafından seçilen yedeği mysql komutu ile geri yüklemek  

---

### 3.4 Yapılandırma Yönetim Modülü (config_editor.py)

Bu modül my.cnf yapılandırma dosyasını düzenlemek için kullanılır.

İşlevleri:
- Yapılandırma dosyasını yedeklemek  
- Belirli parametreleri (ör. max_connections) güncellemek  
- Dosya okuma ve yazma işlemlerini güvenli şekilde gerçekleştirmek  

---

## 4. Veri Akışı

1. Kullanıcı ana menüyü başlatır  
2. Menüden işlem türü seçilir  
3. İlgili modül çağrılır  
4. Sistem komut satırı araçları (mysqldump, mysql) çalıştırılır  
5. Sonuç kullanıcıya raporlanır  

---

## 5. Güvenlik ve Hata Yönetimi

- Kullanıcı bilgileri dosyada saklanmaz  
- Yapılandırma dosyası değiştirilmeden önce yedek alınır  
- Hata durumlarında kullanıcıya açıklayıcı mesajlar gösterilir  

---

## 6. Genişletilebilirlik

Sistem ileride aşağıdaki özelliklerle genişletilebilir:

- PostgreSQL desteği  
- Zamanlayıcı (cron benzeri) entegrasyonu  
- Grafiksel kullanıcı arayüzü  
- Otomatik bulut yedekleme  

---

## 7. Sonuç

Bu mimari yapı sayesinde sistem modüler, bakımı kolay ve genişletilebilir bir yapıya sahiptir. Proje, veritabanı bakım otomasyonunun temel prensiplerini başarıyla uygulamaktadır.
