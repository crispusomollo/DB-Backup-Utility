import gzip
import shutil
import logging

logger = logging.getLogger("dbbackup")

def gzip_file(path):
    gzip_path = f"{path}.gz"
    logger.info(f"Compressing {path} → {gzip_path}")

    with open(path, "rb") as src, gzip.open(gzip_path, "wb") as dst:
        shutil.copyfileobj(src, dst)

    return gzip_path

