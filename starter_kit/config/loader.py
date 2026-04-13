import os
import yaml
from dotenv import load_dotenv

load_dotenv()


def load_config():
    config_path = "config/settings.yaml"

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    config["default_exchange"] = os.getenv(
        "DEFAULT_EXCHANGE",
        config.get("default_exchange"),
    )

    dry_run_env = os.getenv("DRY_RUN")
    if dry_run_env is not None:
        config["dry_run"] = dry_run_env.lower() == "true"

    return config
