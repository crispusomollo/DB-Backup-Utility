import os
from dbbackup.connectors import MySQLConnector, PostgresConnector, DBConnectorError
from dbbackup.compress import compress_file
from dbbackup.logger import logger

def backup_database(config, output_dir='./backups'):
    """Orchestrate backup based on DB type"""
    os.makedirs(output_dir, exist_ok=True)
    dbtype = config.get('dbtype').lower()
    if dbtype == 'mysql':
        connector = MySQLConnector(config)
    elif dbtype == 'postgres':
        connector = PostgresConnector(config)
    else:
        raise NotImplementedError(f"Backup for {dbtype} not implemented yet")
    
    logger.info(f"Testing connection to {dbtype} database...")
    connector.test_connection()
    
    logger.info(f"Starting backup for database: {config.get('database')}")
    backup_file = connector.dump(output_dir)
    
    logger.info(f"Compressing backup file...")
    compressed_file = compress_file(backup_file)
    
    logger.info(f"Backup completed: {compressed_file}")
    return compressed_file

