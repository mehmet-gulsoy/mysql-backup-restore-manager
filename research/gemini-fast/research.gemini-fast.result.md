# Ana Araştırma Sonucu: Veritabanı Bakım Operasyonları

Bu araştırma; Backup, Restore ve Config yönetimi süreçlerinin temel çalışma prensiplerini ve endüstri standartlarını kapsamaktadır.

## Temel Bulgular
- **Yedekleme Stratejileri:** Mantıksal (Logical) ve Fiziksel (Physical) yedekleme arasındaki farklar incelenmiş, küçük/orta ölçekli projeler için taşınabilirlik açısından mantıksal yedeklemenin (.sql dump) önemi vurgulanmıştır.
- **En İyi Uygulamalar:** 3-2-1 kuralı ve PITR (Noktasal Geri Dönüş) mekanizmaları araştırılmıştır.
- **Konfigürasyon Yönetimi:** MySQL (`my.cnf`) ve PostgreSQL (`postgresql.conf`) üzerindeki kritik performans parametreleri (buffer_pool, shared_buffers, max_connections) listelenmiştir.
- **Güvenlik:** Yedeklerin şifrelenmesi (Encryption at rest) ve "En Az Yetki İlkesi" (Principle of Least Privilege) ile veritabanı kullanıcılarının yönetilmesi gerekliliği saptanmıştır.

## Rakip Analizi
Barman (PostgreSQL), Percona XtraBackup (MySQL) ve pgAdmin gibi açık kaynaklı araçlar, kullanıcı arayüzü ve fonksiyonellik açısından referans alınmıştır.