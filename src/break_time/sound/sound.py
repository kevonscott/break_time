import os
from pathlib import Path

import playsound


class Sound:
    def __init__(self, filename="metal_gear_alert.mp3", test=False) -> None:
        self.test = test
        self.file_location = (
            Path(__file__).parent / ".." / "static" / "sound" / filename
        ).resolve()
        if not os.path.exists(self.file_location):
            raise FileNotFoundError

    def play(self):
        if self.test:
            return None
        else:
            playsound.playsound(self.file_location)
