# Copilot Araştırma Sonucu

## 1. Temel Çalışma Prensipleri
- **Backup:** `mysqldump` ve `pg_dump` ile logical backup; `xtrabackup` ve `pg_basebackup` ile physical backup.
- **Restore:** SQL dump dosyalarının `mysql < dump.sql` veya `psql < dump.sql` ile yüklenmesi; büyük verilerde PITR.
- **Config:** MySQL için `my.cnf`, PostgreSQL için `postgresql.conf` dosyaları.

## 2. Best Practices
- Düzenli otomatik yedekleme (cron job).
- Yedeklerin test restore edilmesi.
- Config dosyalarının versiyon kontrolü (Git).
- Performans parametrelerinin optimize edilmesi.

## 3. Açık Kaynak Projeler
- Percona XtraBackup (MySQL/MariaDB)
- pgBackRest (PostgreSQL)
- Barman (PostgreSQL)
- MyDumper/MyLoader (MySQL)
- Wal-G (PostgreSQL/MySQL)

## 4. Kritik Parametreler
- **MySQL (`my.cnf`):** `innodb_buffer_pool_size`, `max_connections`, `slow_query_log`, `binlog_format`
- **PostgreSQL (`postgresql.conf`):** `shared_buffers`, `work_mem`, `wal_level`, `max_connections`, `logging_collector`

## 5. Güvenlik Noktaları
- Yedeklerin şifrelenmesi (GPG, OpenSSL).
- Erişim kontrolü ve yetkilendirme.
- SSL/TLS ile güvenli transfer.
- Config dosyalarında parola saklamama.
- Audit loglarının tutulması.
