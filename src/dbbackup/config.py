import os
import yaml

def load_config(path: str):
    """
    Loads YAML configuration and merges with environment variables.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")

    with open(path, "r") as f:
        data = yaml.safe_load(f)

    # Merge ENV overrides
    for section, values in data.items():
        for key in values:
            env_key = f"{section.upper()}_{key.upper()}"
            if env_key in os.environ:
                data[section][key] = os.environ[env_key]

    return data

