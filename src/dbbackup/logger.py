import logging
import sys

def init_logger(level=logging.INFO):
    """
    Initializes a simple but structured logger.
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    return logging.getLogger("dbbackup")

