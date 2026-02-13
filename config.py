from pathlib import Path
import json

def create_config(ai_provider="", api_key="", model="", ai_enabled=False, storage_dir="./"):
    storage_path = Path(storage_dir) / "tasks.json"
    return {
        "main": {
            "storage": str(storage_path)
        },
        "ai": {
            "enabled": ai_enabled,
            "provider": ai_provider,
            "model": model,
            "api_key": api_key
        }
    }

def save_config(config):
    with open("config.json", "w") as config_file:
        json.dump(config, config_file, indent=4)

def load_config(config_path="config.json"):
    with open(config_path, "r") as config_file:
        return json.load(config_file)

def check_config():
    config_path = Path("config.json")
    return Path.exists(config_path)