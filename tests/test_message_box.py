import sys
import unittest
sys.path.append('../break_time/')  # append parent dir to import sound module
from break_time.message_box import MessageBox

class TestMethods(unittest.TestCase):
    def test_display(self):
        message_box_obj = MessageBox(message='TMessage', subject='TSubject', test=True)
        self.assertEqual(None, message_box_obj.display())

if __name__=='__main__':
    unittest.main()