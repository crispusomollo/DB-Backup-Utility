# DB Backup Utility

A modular, cross-DBMS backup and restore CLI tool with cloud upload, compression, logging, and scheduler support.

---

# 1. Overview

The **DB Backup Utility** is a Python-based command-line tool that supports backing up and restoring multiple database types, including:

* MySQL
* PostgreSQL
* MongoDB
* SQLite (coming soon)

The tool supports:

* Full backups
* Selective table restore (MySQL/PostgreSQL)
* Compression (gzip)
* Local + cloud storage (S3, GCS, Azure)
* Automated scheduled backups via systemd or APScheduler
* YAML-based configuration

This documentation provides complete instructions for installation, configuration, usage, automation, and troubleshooting.

---

# 2. Features

### ✔ Multi-Database Support

* MySQL (`mysqldump`)
* PostgreSQL (`pg_dump`)
* MongoDB (`mongodump`)
* SQLite (planned)

### ✔ Backup Options

* Full database dumps
* Incremental backup (DB-supported engines only)
* Differential backup (future)
* Optional compression (`.gz`)

### ✔ Restore Options

* Full DB restore
* Selective-table restore for:

  * MySQL
  * PostgreSQL

### ✔ Storage Options

* Local filesystem
* Cloud:

  * AWS S3
  * Google Cloud Storage
  * Azure Blob Storage

### ✔ Automation

* APScheduler-based in-app scheduler
* systemd service + timer (recommended for servers)

### ✔ Logging + Notifications

* Detailed logs (start, end, duration, errors)
* Slack notifications (optional)

---

# 3. Architecture

```
db-backup-utility/
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── src/dbbackup/
│   ├── cli_click.py
│   ├── cli_typer.py
│   ├── config.py
│   ├── logger.py
│   ├── connectors.py
│   ├── backup.py
│   ├── restore.py
│   ├── storage.py
│   ├── compress.py
│   └── scheduler.py
├── examples/
│   ├── mysql.example.yml
│   ├── postgres.example.yml
│   └── mongodb.example.yml
└── scripts/
    ├── install.sh
    └── systemd/
        ├── dbbackup.service
        └── dbbackup.timer
```

---

# 4. Installation

## Requirements

* Python 3.9+
* `mysqldump` (for MySQL backups)
* `pg_dump` and `psql` (PostgreSQL)
* `mongodump` and `mongorestore` (MongoDB)

## Install from source

```bash
git clone https://github.com/crispusomollo/db-backup-utility
cd db-backup-utility
pip install -r requirements.txt
pip install .
```

## Install with the included script

```bash
chmod +x scripts/install.sh
sudo ./scripts/install.sh
```

---

# 5. Configuration

All settings are stored in a YAML file.

Example (MySQL):

```yaml
database:
  engine: mysql
  host: localhost
  port: 3306
  user: root
  password: secret
  name: companydb

backup:
  output_dir: /var/backups/db
  compression: true

storage:
  enabled: true
  provider: s3
  bucket: my-backups-bucket
  aws_access_key: KEY
  aws_secret_key: SECRET

restore:
  file: /var/backups/db/companydb_2024.gz

schedule:
  cron:
    minute: "0"
    hour: "2"
```

---

# 6. CLI Usage

The CLI supports Click and Typer interfaces (`dbbackup` command exposes Click).

### Help

```bash
dbbackup --help
```

---

# 7. Backup Operations

## Full Backup

```bash
dbbackup backup -c config.yml
```

## Backup Without Compression

```bash
dbbackup backup -c config.yml --no-compress
```

## Backup With Cloud Upload Only

```bash
dbbackup backup -c config.yml --cloud-only
```

---

# 8. Restore Operations

## Full Restore

```bash
dbbackup restore -c config.yml
```

## Selective Table Restore (MySQL)

```bash
dbbackup restore -c mysql.yml --tables employees,departments
```

## Selective Table Restore (PostgreSQL)

```bash
dbbackup restore -c postgres.yml --tables public.users,public.logs
```

---

# 9. Storage Options

## Local Storage

Done automatically to `backup.output_dir`.

## AWS S3 Upload

```yaml
storage:
  enabled: true
  provider: s3
```

## Google Cloud Storage

```yaml
storage:
  provider: gcs
  bucket: db-backups
```

## Azure Blob Storage

```yaml
storage:
  provider: azure
  container: backups
```

---

# 10. Logging

Logs are saved to:

```
/var/log/dbbackup/dbbackup.log
```

Log fields include:

* Start time
* End time
* Duration
* DB engine
* Exit status
* Uploaded cloud location (if any)
* Errors

---

# 11. Scheduling

## Using systemd (recommended)

### Install service + timer:

```
sudo cp scripts/systemd/dbbackup.service /etc/systemd/system/
sudo cp scripts/systemd/dbbackup.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now dbbackup.timer
```

### Check status:

```
systemctl status dbbackup.timer
```

## Using APScheduler (built-in)

Add to YAML:

```yaml
schedule:
  cron:
    hour: "2"
    minute: "0"
```

Run:

```
dbbackup scheduler -c config.yml
```

---

# 12. Troubleshooting

### “mysqldump not found”

Install MySQL client tools.

### “pg_dump: command not found”

Install PostgreSQL client:

```
sudo apt install postgresql-client
```

### “Access Denied” on AWS S3

Check IAM permissions:

* `s3:PutObject`
* `s3:GetObject`

### Backups too slow

* Disable compression
* Use local SSD storage
* Run backups on replica DB

---

# 13. Contributing

Pull requests are welcome.

Rules:

* PEP8 compliance
* Add unit tests for new functions
* Use type hints
* Document new features in README

---

# 14. License

MIT License © 2025

