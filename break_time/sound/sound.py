from pathlib import Path

from playsound import playsound


class Sound:
    def __init__(self, filename="metal_gear_alert.mp3", test=False) -> None:
        self.test = test
        self.file_location = (
            Path(__file__).parent.parent / "static" / "audio" / filename
        ).resolve()
        if not self.file_location.exists():
            raise FileNotFoundError

    def play(self):
        if self.test:
            return None
        else:
            playsound(str(self.file_location))
