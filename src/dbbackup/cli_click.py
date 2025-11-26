import click
from .config import load_config
from .backup import run_backup
from .restore import run_restore
from .logger import init_logger

@click.group()
@click.option("--config", "-c", default="config.yml", help="Path to configuration file.")
@click.pass_context
def cli(ctx, config):
    """Database Backup Utility (Click CLI)."""
    ctx.ensure_object(dict)
    ctx.obj["config_path"] = config
    init_logger()

@cli.command()
@click.pass_context
def backup(ctx):
    """Run a database backup."""
    cfg = load_config(ctx.obj["config_path"])
    run_backup(cfg)

@cli.command()
@click.pass_context
def restore(ctx):
    """Restore a database backup."""
    cfg = load_config(ctx.obj["config_path"])
    run_restore(cfg)

if __name__ == "__main__":
    cli()

