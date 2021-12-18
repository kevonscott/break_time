import tkinter as tk
from tkinter import ttk
import pkg_resources
import json

from utils.activity import new_alert


class BreakTime(object):
    def __init__(self):
        self.window = tk.Tk()  # Main/Root Tk window
        # Configure root window
        self.window.title("BreakTime")
        self.window.rowconfigure(0, minsize=50, weight=1)
        self.window.columnconfigure([0, 1, 2], minsize=50, weight=1)

        self.config = self._load_config()  # Stores the configuration data
        self.counter_is_active = False  # Decide if counter is active of not
        self.counter = self.config.get("interval")
        print(f"Timer initiated to {self.counter}")

        # On and Off mages for the auto start button
        self.ON_IMG = tk.PhotoImage(
            file=pkg_resources.resource_filename(__name__, "../data/image/on.png")
        )
        self.OFF_IMG = tk.PhotoImage(
            file=pkg_resources.resource_filename(__name__, "../data/image/off.png")
        )

        self.intervals = [
            10,
            15,
            20,
            25,
            30,
            35,
            40,
            45,
            50,
            55,
            60,
            65,
            70,
            75,
            80,
            85,
            90,
            95,
            100,
            105,
            110,
            115,
            120,
        ]
        self.style = ttk.Style()

        self.messagebox_is_active = False

        # Create the widgets
        self.create_widgets()

    def run(self):
        """Run the application"""
        if self.config.get("auto-start"):
            self._start()

        self.window.mainloop()

    def create_widgets(self):
        # I am using a 3 column grid design. Thus a function to create the grid
        # for each column
        grid_left = self._create_left_grid(master_frame=self.window)  # Col 0
        grid_middle = self._create_middle_grid(master_frame=self.window)  # Col 1
        grid_right = self._create_right_grid(master_frame=self.window)  # Col 2

        # packing all the frames  together in a grid
        # info_frame.grid(row=0, column=0, pady=10)
        grid_left.grid(row=0, column=0, padx=10, pady=10)
        grid_middle.grid(row=0, column=1, padx=10, pady=10)
        grid_right.grid(row=0, column=2, padx=10, pady=10)

    def _create_left_grid(self, master_frame):
        """Create the grid for the left column

        Parameters
        ----------
        master_frame : tkinter.Frame
            The master frame for the column

        Returns
        -------
        tkinter.Frame
            The left frame(column)
        """
        btn_frame = tk.Frame(master=master_frame)
        if self.config.get("auto-start"):
            auto_start_color = "green"
            self.btn_auto_start_ = tk.Button(
                master=btn_frame,
                font=("Helvetica", 10),
                image=self.ON_IMG,
                bd=0,
                command=self._update_auto_start_button,
            )
        else:
            auto_start_color = "red"
            self.btn_auto_start_ = tk.Button(
                master=btn_frame,
                font=("Helvetica", 10),
                image=self.OFF_IMG,
                bd=0,
                command=self._update_auto_start_button,
            )
        self.lbl_auto_start_ = tk.Label(
            master=btn_frame, text="Auto-Start", fg=auto_start_color
        )
        btn_start = tk.Button(master=btn_frame, text="Start/Reset", command=self._start)
        btn_stop = tk.Button(master=btn_frame, text="Stop", command=self._stop)
        btn_continue = tk.Button(
            master=btn_frame, text="Continue", command=self._continue
        )

        self.lbl_auto_start_.grid(row=0, column=0, sticky="N")
        self.btn_auto_start_.grid(row=0, column=1, sticky="N")

        btn_start.grid(row=1, column=0, padx=5, pady=15)
        btn_continue.grid(row=1, column=1, padx=5, pady=15)
        btn_stop.grid(row=1, column=2, padx=5, pady=15)

        return btn_frame

    def _create_middle_grid(self, master_frame):
        """Create a frame for the middle column

        Parameters
        ----------
        master_frame : tkinter.Frame
            The master frame for the column

        Returns
        -------
        tkinter.Frame
            The middle frame(column)
        """
        self.style.configure("TMenubutton", font=("Helvetica", 10, "bold"))

        counter_frame = tk.Frame(master=master_frame)
        interval_frame = tk.Frame(master=counter_frame)
        interval_frame.grid(row=0, column=0, sticky="EW")

        variable = tk.IntVar(master=counter_frame)
        lbl_interval = ttk.OptionMenu(
            interval_frame, variable, *self.intervals, command=self._set_interval
        )
        variable.set(self.config.get("interval"))
        lbl_interval.grid(row=0, column=0)
        lbl_unit = tk.Label(
            master=interval_frame, text="minutes", font=("Helvetica", 10)
        )
        lbl_unit.grid(row=0, column=1)

        self.lbl_counter_ = tk.Label(
            master=counter_frame,
            text=self.counter,
            fg="red",
            font=("Helvetica", 70),
            relief="ridge",
            border=10,
        )
        self.lbl_counter_.grid(row=1, column=0, pady=10)

        return counter_frame

    def _create_right_grid(self, master_frame):
        """Create a frame for the right column

        Parameters
        ----------
        master_frame : tkinter.Frame
            The master frame for the column

        Returns
        -------
        tkinter.Frame
            The right frame(column)
        """
        config_frame = tk.Frame(master=master_frame)
        sound_frame = tk.LabelFrame(master=config_frame, text="Select Audio")
        sound_frame.grid(row=0, column=0)
        self._load_audio_files(master_frame=sound_frame)
        btn_update = tk.Button(
            master=config_frame, text="Save", command=self._update_config
        )
        btn_update.grid(row=1, column=0, pady=10, sticky="EW")

        return config_frame

    def _load_audio_files(self, master_frame):
        """Load the audio files and create RadioButton selection(s) in the master_frame

        Parameters
        ----------
        master_frame : tkinter.Frame
            The master frame to pack the RadioButtons on.
        """

        def _update_audio_config():
            choice = v.get()
            print(f"Updating audio config to {choice}")
            self.config["default-audio"] = choice

        v = tk.StringVar()
        files = pkg_resources.resource_listdir(__name__, "../data/sound")
        if not files:
            raise FileNotFoundError("No Audio file(s) found...")
        for value in files:
            x = tk.Radiobutton(
                master=master_frame,
                text=value,
                value=value,
                variable=v,
                command=_update_audio_config,
            )
            x.grid(sticky="W")
            # set default value
            if value == self.config.get("default-audio"):
                print(f"Default audio is {value}")
                v.set(value)

    def _update_auto_start_button(self):
        """Checks and updates auto start button"""
        if self.config.get("auto-start"):
            self.btn_auto_start_.config(image=self.OFF_IMG)
            self.lbl_auto_start_.config(fg="red")
            print("Setting Auto-Start to False")
            self.config["auto-start"] = False
        else:
            self.btn_auto_start_.config(image=self.ON_IMG)
            self.lbl_auto_start_.config(fg="green")
            print("Setting Auto-Start to True")
            self.config["auto-start"] = True

    def _count_down(self):
        """Start the countdown timer"""
        time_delta = 1000  # every second
        if self.counter_is_active:
            self.lbl_counter_["text"] = str(self.counter)
            self.counter -= 1
            if self.counter < 0:
                # make alert
                if self.messagebox_is_active:
                    print("Activity box already active, skipping....")
                else:
                    self.messagebox_is_active = True
                    # Make the alert and reset active state
                    new_alert(audio_filename=self.config.get("default-audio"))
                    self.messagebox_is_active = False
                # Reset Counter
                self.counter = self.config.get("interval")
            self.window.after(time_delta, self._count_down)

    def _start(self):
        """Start the countdown timer"""
        self.counter_is_active = True
        self.counter = self.config.get("interval")
        self._count_down()

    def _stop(self):
        """Stop the countdown timer"""
        self.counter_is_active = False

    def _continue(
        self,
    ):
        """Continue the countdown timer from where it last stopped"""
        self.counter_is_active = True
        self._count_down()

    def _set_interval(self, *args):
        print(f"Updating interval to {args[0]}")
        self.config["interval"] = args[0]
        self.lbl_counter_["text"] = str(args[0])

    def _load_config(self):
        """Function to read in configuration and initialize counter"""
        with open(
            pkg_resources.resource_filename(__name__, "config/break_time.json"), "r"
        ) as cfg_file:
            config_data = json.load(cfg_file)
        return config_data

    def _update_config(self):
        """Update the configuration data"""
        print("updating config file...")
        with open(
            pkg_resources.resource_filename(__name__, "config/break_time.json"), "w"
        ) as cfg_file:
            json.dump(self.config, cfg_file)
