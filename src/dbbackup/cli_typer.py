import typer
from .config import load_config
from .backup import run_backup
from .restore import run_restore
from .logger import init_logger

app = typer.Typer(help="Database Backup Utility (Typer CLI)")

@app.callback()
def main(
    config: str = typer.Option("config.yml", "--config", "-c", help="Path to config file.")
):
    init_logger()
    typer.echo(f"Using config: {config}")

@app.command()
def backup(config: str = "config.yml"):
    cfg = load_config(config)
    run_backup(cfg)
    typer.echo("Backup complete.")

@app.command()
def restore(config: str = "config.yml"):
    cfg = load_config(config)
    run_restore(cfg)
    typer.echo("Restore complete.")

if __name__ == "__main__":
    app()
