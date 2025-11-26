import subprocess
import logging

logger = logging.getLogger("dbbackup")

def test_connection(cfg):
    """
    Test DB connection using CLI tools.
    Supports: mysql, postgres
    """
    engine = cfg["database"]["engine"]

    if engine == "mysql":
        cmd = [
            "mysql",
            "-h", cfg["database"]["host"],
            "-u", cfg["database"]["user"],
            f"-p{cfg['database']['password']}",
            "-e", "SELECT 1;"
        ]

    elif engine == "postgres":
        cmd = [
            "psql",
            f"postgresql://{cfg['database']['user']}:{cfg['database']['password']}@"
            f"{cfg['database']['host']}:{cfg['database']['port']}/{cfg['database']['name']}",
            "-c", "SELECT 1;"
        ]
    else:
        raise ValueError(f"Unsupported engine: {engine}")

    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        logger.info("Connection successful.")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Connection failed: {e.output.decode()}")
        return False

