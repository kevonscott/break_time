import sys
import unittest
sys.path.append('../break_time/')  # append parent dir to import sound module
from break_time.sound.sound import Sound

class TestMethods(unittest.TestCase):
    def test_sound_file_not_found(self):
        none_existing_file = 'sfsfaukjskfihjwwfkas.mp3'
        self.assertRaises(FileNotFoundError, Sound, none_existing_file)
    
    def test_sound_play(self):
        file_name = 'metal_gear_alert.mp3'
        sound_obj = Sound(filename=file_name, test=True)
        self.assertEqual(None, sound_obj.play())

if __name__=='__main__':
    unittest.main()