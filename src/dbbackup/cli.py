import click
from dbbackup import logger
from dbbackup.config import load_config
from dbbackup.backup import backup_database
from dbbackup.restore import restore_database

@click.group()
def cli():
    """Database Backup Utility CLI"""
    pass

@cli.command()
@click.option('--dbtype', required=True, type=click.Choice(['mysql','postgres','mongodb','sqlite']))
@click.option('--host', default='localhost', help='Database host')
@click.option('--port', default=None, type=int, help='Database port')
@click.option('--username', help='Database user')
@click.option('--password', help='Database password')
@click.option('--database', help='Database name')
@click.option('--backup-path', default='./backups', help='Path to store backups')
def backup(dbtype, host, port, username, password, database, backup_path):
    """Backup a database"""
    config = {
        'dbtype': dbtype,
        'host': host,
        'port': port,
        'username': username,
        'password': password,
        'database': database
    }
    try:
        backup_file = backup_database(config, backup_path)
        click.echo(f"Backup completed: {backup_file}")
    except Exception as e:
        logger.logger.error(f"Backup failed: {e}")
        click.echo(f"Backup failed: {e}")

@cli.command()
@click.option('--dbtype', required=True, type=click.Choice(['mysql','postgres','mongodb','sqlite']))
@click.option('--host', default='localhost', help='Database host')
@click.option('--port', default=None, type=int, help='Database port')
@click.option('--username', help='Database user')
@click.option('--password', help='Database password')
@click.option('--database', help='Database name')
@click.option('--backup-path', required=True, help='Backup file path to restore')
@click.option('--tables', default=None, help='Comma-separated list of tables to restore (optional)')
def restore(dbtype, host, port, username, password, database, backup_path, tables):
    """Restore a database"""
    config = {
        'dbtype': dbtype,
        'host': host,
        'port': port,
        'username': username,
        'password': password,
        'database': database
    }
    table_list = tables.split(',') if tables else None
    try:
        restore_database(config, backup_path, table_list)
        click.echo(f"Restore completed successfully.")
    except Exception as e:
        logger.logger.error(f"Restore failed: {e}")
        click.echo(f"Restore failed: {e}")

if __name__ == "__main__":
    cli()

