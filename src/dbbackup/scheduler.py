from apscheduler.schedulers.background import BackgroundScheduler
import logging
from .backup import run_backup
from .config import load_config

logger = logging.getLogger("dbbackup")

def start_scheduler(config_path="config.yml"):
    cfg = load_config(config_path)
    scheduler = BackgroundScheduler()

    cron = cfg["schedule"]["cron"]

    scheduler.add_job(
        run_backup,
        "cron",
        args=[cfg],
        minute=cron.get("minute", "0"),
        hour=cron.get("hour", "*"),
        day=cron.get("day", "*"),
        month=cron.get("month", "*"),
        day_of_week=cron.get("weekday", "*"),
    )

    logger.info("Backup scheduler started.")
    scheduler.start()

