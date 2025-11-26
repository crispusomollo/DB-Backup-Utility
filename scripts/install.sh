#!/bin/bash
set -e

echo "=== Database Backup Utility Installer ==="

# 1️⃣ Ask user which CLI to use
echo "Select CLI version to install:"
echo "1) Click CLI (stable, fewer dependencies)"
echo "2) Typer CLI (modern, type-hints, rich formatting)"
read -p "Enter choice [1 or 2]: " cli_choice

if [[ "$cli_choice" != "1" && "$cli_choice" != "2" ]]; then
    echo "Invalid choice. Exiting."
    exit 1
fi

# 2️⃣ Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3️⃣ Upgrade pip
pip install --upgrade pip

# 4️⃣ Install dependencies
if [[ "$cli_choice" == "1" ]]; then
    echo "Installing Click CLI dependencies..."
    pip install -r requirements-click.txt
    CLI_CMD="python -m dbbackup.cli_click"
else
    echo "Installing Typer CLI dependencies..."
    pip install -r requirements-typer.txt
    CLI_CMD="python -m dbbackup.cli_typer"
fi

# 5️⃣ Create backups directory
mkdir -p ./backups

echo "----------------------------------------"
echo "Installation complete!"
echo "Activate virtual environment: source .venv/bin/activate"
echo "Run CLI: $CLI_CMD --help"
echo "Backup directory: ./backups"
echo "----------------------------------------"

