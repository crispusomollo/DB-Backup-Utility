from apscheduler.schedulers.background import BackgroundScheduler
from dbbackup.logger import logger

scheduler = BackgroundScheduler()

def schedule_backup(func, trigger='interval', **kwargs):
    """Schedule backup task"""
    scheduler.add_job(func, trigger, **kwargs)
    logger.info(f"Scheduled backup: {func.__name__} with {trigger} {kwargs}")
    scheduler.start()

