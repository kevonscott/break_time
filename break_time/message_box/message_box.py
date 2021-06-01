import ctypes

class MessageBox:
    def __init__(self, message, subject, test=False) -> None:
        self.message = message
        self.subject = subject
        self.test = test
        
    def display(self):
        """Function to display a pop box on a window environment.
        """
        # Create a popup message box
        popup_box = ctypes.windll.user32.MessageBoxW
        if self.test:
            return None
        else:
            #  48 = MB_ICONEXCLAMATION (0x00000030L) An exclamation-point icon 
            # appears in the message box.
            popup_box(None, self.message, self.subject, 48) 