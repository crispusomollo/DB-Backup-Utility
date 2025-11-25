# Database Backup Utility (CLI Tool)

![GitHub repo size](https://img.shields.io/github/repo-size/crispusomollo/DB-Backup-Utility)
![GitHub last commit](https://img.shields.io/github/last-commit/crispusomollo/DB-Backup-Utility?color=blue)
![GitHub issues](https://img.shields.io/github/issues/crispusomollo/DB-Backup-Utility?color=yellow)
![GitHub pull requests](https://img.shields.io/github/issues-pr/crispusomollo/DB-Backup-Utility?color=brightgreen)
![GitHub contributors](https://img.shields.io/github/contributors/crispusomollo/DB-Backup-Utility?color=orange)
![GitHub stars](https://img.shields.io/github/stars/crispusomollo/DB-Backup-Utility?style=social)

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![License](https://img.shields.io/github/license/crispusomollo/DB-Backup-Utility)
![Build Status](https://img.shields.io/github/actions/workflow/status/crispusomollo/DB-Backup-Utility/ci.yml?label=CI%20Build)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

A cross-platform command-line utility for **backing up and restoring databases** (MySQL, PostgreSQL, MongoDB, SQLite).
Includes compression, S3/GCS/Azure storage, logging, scheduling, and selective-table restore.

## Quick Start

```bash
git clone https://github.com/crispusomollo/DB-Backup-Utility.git
cd DB-Backup-Utility
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m dbbackup.cli --help
```

## Features

- Multi-DB support: MySQL, PostgreSQL, MongoDB, SQLite

- Selective-table restore (MySQL & PostgreSQL)

- Compression (.tar.gz)

- Local and cloud storage (AWS S3, Google Cloud Storage, Azure Blob)

- Logging and optional Slack notifications

- Scheduling support (cron/systemd/Task Scheduler)


## Usage examples

Full backup:
```
python -m dbbackup.cli backup --dbtype postgres --host localhost --username admin --database mydb
```

Selective-table restore:
```
python -m dbbackup.cli restore --dbtype postgres --host localhost --username admin --database mydb --backup-path /backups/mydb.dump --tables users,orders
```

## Project Layout

```
db-backup-utility/
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── src/
│   ├── dbbackup/
│   │   ├── __init__.py
│   │   ├── cli.py            # entrypoint (Click)
│   │   ├── config.py         # config parsing (YAML/ENV)
│   │   ├── logger.py         # centralized logging
│   │   ├── connectors.py     # DB connector + test_connection
│   │   ├── backup.py         # backup orchestration
│   │   ├── restore.py        # restore orchestration
│   │   ├── storage.py        # local & cloud (S3, GCS, Azure) upload/download
│   │   ├── compress.py       # gzip / tar / zip helpers
│   │   └── scheduler.py      # APScheduler wrapper (optional)
├── examples/
│   ├── mysql.example.yml
│   ├── postgres.example.yml
│   └── mongodb.example.yml
└── scripts/
    ├── install.sh
    └── systemd/ (service + timer example)
```

## License

MIT

