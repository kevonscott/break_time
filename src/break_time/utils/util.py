import json
from pathlib import Path

CONFIG_FILE = Path(__file__).parent.parent / "config/break_time.json"


def load_config() -> dict:
    """Function to read in configuration and initialize counter"""
    with open(CONFIG_FILE, "r") as cfg_file:
        config_data = json.load(cfg_file)
    return config_data


def update_config(config: dict) -> None:
    current_config = load_config()
    current_config.update(config)  # TODO: validate before updating config

    with open(CONFIG_FILE, "w") as cfg_file:
        json.dump(current_config, cfg_file)


def load_audio_files() -> list[str]:
    """Load the audio files."""
    audio_assets_path = Path(__file__).parent.parent / "static/audio"
    if not audio_assets_path.exists():
        raise FileNotFoundError(
            f"Could not locate audio assets directory: {audio_assets_path}"
        )
    return [f.name for f in audio_assets_path.iterdir()]
