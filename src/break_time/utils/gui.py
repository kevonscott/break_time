import customtkinter as ctk

from .frames import ControlFrame, CounterFrame, OptionsFrame


class BreakTime(ctk.CTk):
    """Main application."""

    def __init__(self, log):
        super().__init__()
        self.title("BreakTime")
        self.geometry()  # not specifying size, let it auto adjust
        self.log = log
        self.grid_column_shape = (0, 1, 2)  # Using a 3 column grid design
        self.grid_rowconfigure(0, minsize=50, weight=1)
        self.grid_columnconfigure(self.grid_column_shape, minsize=50, weight=1)

        self._create_widgets()  # Create the widgets

    def launch(self) -> None:
        """Run the application"""
        self.mainloop()

    def _create_widgets(self) -> None:
        """Create each Frame and attach to the grid."""

        # Frame for controlling the apps display counter
        counter_frame: ctk.CTkFrame = CounterFrame(master=self, log=self.log)
        counter_frame.grid(row=0, column=1, padx=10, pady=10)

        # Frame for controlling the app
        control_frame: ctk.CTkFrame = ControlFrame(
            master=self, counter_frame=counter_frame, log=self.log
        )
        control_frame.grid(row=0, column=0, padx=10, pady=10)

        # Frame for the apps other options such as theme, music etc..
        options_frame: ctk.CTkFrame = OptionsFrame(master=self, log=self.log)
        options_frame.grid(row=0, column=2, padx=10, pady=10)
