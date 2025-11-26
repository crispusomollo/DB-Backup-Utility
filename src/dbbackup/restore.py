from dbbackup.connectors import MySQLConnector, PostgresConnector
from dbbackup.logger import logger

def restore_database(config, backup_path, tables=None):
    """Orchestrate restore based on DB type"""
    dbtype = config.get('dbtype').lower()
    if dbtype == 'mysql':
        connector = MySQLConnector(config)
    elif dbtype == 'postgres':
        connector = PostgresConnector(config)
    else:
        raise NotImplementedError(f"Restore for {dbtype} not implemented yet")
    
    logger.info(f"Testing connection to {dbtype} database...")
    connector.test_connection()
    
    logger.info(f"Starting restore from backup: {backup_path}")
    connector.restore(backup_path, tables)
    logger.info(f"Restore completed successfully.")

