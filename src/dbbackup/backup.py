import os
import datetime
import subprocess
import logging
from .compress import gzip_file
from .storage import upload_to_storage
from .connectors import test_connection

logger = logging.getLogger("dbbackup")

def generate_backup_filename(cfg):
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    engine = cfg["database"]["engine"]
    db = cfg["database"]["name"]
    return f"{engine}_{db}_{timestamp}.sql"

def run_backup(cfg):
    if not test_connection(cfg):
        logger.error("Backup aborted: DB connection failed.")
        return

    engine = cfg["database"]["engine"]
    filename = generate_backup_filename(cfg)
    output_path = os.path.join(cfg["backup"]["output_dir"], filename)

    os.makedirs(cfg["backup"]["output_dir"], exist_ok=True)

    logger.info(f"Backing up database to: {output_path}")

    if engine == "mysql":
        cmd = [
            "mysqldump",
            "-h", cfg["database"]["host"],
            "-u", cfg["database"]["user"],
            f"-p{cfg['database']['password']}",
            cfg["database"]["name"],
        ]

    elif engine == "postgres":
        cmd = [
            "pg_dump",
            f"postgresql://{cfg['database']['user']}:{cfg['database']['password']}@"
            f"{cfg['database']['host']}:{cfg['database']['port']}/{cfg['database']['name']}"
        ]

    else:
        raise ValueError(f"Unsupported engine: {engine}")

    try:
        with open(output_path, "wb") as f:
            subprocess.check_call(cmd, stdout=f)

        # Optional compression
        if cfg["backup"].get("compression", True):
            compressed_path = gzip_file(output_path)
            os.remove(output_path)
            output_path = compressed_path
            logger.info(f"Compressed to: {output_path}")

        # Optional cloud upload
        if cfg["storage"].get("enabled", False):
            upload_to_storage(output_path, cfg)

        logger.info("Backup completed successfully.")

    except subprocess.CalledProcessError as e:
        logger.error(f"Backup failed: {e}")


