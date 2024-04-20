import unittest

from break_time.utils.util import load_audio_files


class TestAudioTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.audio_assets = load_audio_files()

    def test_sound_file_not_found(self):
        none_existing_file = "fake-file.mp3"
        self.assertFalse(none_existing_file in self.audio_assets)

    def test_only_mp3(self):
        for file in self.audio_assets:
            self.assertTrue(file.endswith(".mp3"))
