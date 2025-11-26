import os
import tarfile
from dbbackup.logger import logger

def compress_file(file_path):
    """Compress file using tar.gz and return new filename"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")
    
    compressed_file = f"{file_path}.tar.gz"
    with tarfile.open(compressed_file, "w:gz") as tar:
        tar.add(file_path, arcname=os.path.basename(file_path))
    logger.info(f"Compressed {file_path} -> {compressed_file}")
    return compressed_file

