from abc import ABC, abstractmethod
from pathlib import Path

import customtkinter as ctk
from PIL import Image

from .activity import new_alert
from .util import load_config, update_config

CONFIG: dict = load_config()


class CounterFrameMixin(ABC):
    @abstractmethod
    def update_display_counter(self, value: str):
        raise NotImplementedError


class ControlFrame(ctk.CTkFrame):
    def __init__(self, master, counter_frame: ctk.CTkFrame, log):
        super().__init__(master)
        self.log = log
        self.master = master
        self.counter_frame = counter_frame
        self.counter_is_active = False

        self.auto_start: bool = CONFIG["auto-start"]
        self.counter: int = int(CONFIG["interval"])  # Interval Minutes
        self.messagebox_is_active = False
        # On and Off images for the auto start button
        self.ON_IMG = ctk.CTkImage(
            dark_image=Image.open(Path(__file__).parent.parent / "static/image/on.png")
        )
        self.OFF_IMG = ctk.CTkImage(
            dark_image=Image.open(Path(__file__).parent.parent / "static/image/off.png")
        )

        self.start_button = ctk.CTkButton(self, text="Start", command=self._start)
        self.start_button.grid(row=0, column=1, padx=5, pady=15, sticky="w")

        self.reset_button = ctk.CTkButton(self, text="Reset", command=self._reset)
        self.reset_button.grid(row=1, column=0, padx=5, pady=15, sticky="w")

        self.stop_button = ctk.CTkButton(self, text="Stop", command=self._stop)
        self.stop_button.grid(row=1, column=1, padx=5, pady=15, sticky="w")

        self.auto_start_button = ctk.CTkButton(
            self,
            text="Auto-Start",
            font=("Helvetica", 10),
            image=self.ON_IMG if self.auto_start else self.OFF_IMG,
            command=self._update_auto_start_button,
        )
        self.auto_start_button.grid(row=0, column=0, padx=2, pady=15, sticky="ew")

        # Automatically, start the timer is 'auto-start' configured.
        if self.auto_start:
            self._start()

    def _start(self) -> None:
        """Start the countdown timer"""
        if self.counter_is_active:
            self.log.info(
                "Counter already active, nothing to do. Try resetting instead."
            )
        else:
            self.log.info(" Starting counter...")
            self.counter_is_active = True
            self.counter = int(CONFIG["interval"])
            self._count_down()

    def _stop(self) -> None:
        """Stop the countdown timer"""
        self.counter_is_active = False

    def _reset(self) -> None:
        """Stop the countdown timer"""
        self._stop()
        self.counter = int(CONFIG["interval"])
        self._start()

    def _update_auto_start_button(self) -> None:
        """Checks and updates auto start button"""
        if CONFIG["auto-start"]:
            self.auto_start_button.configure(image=self.OFF_IMG)
            self.log.info(" Setting Auto-Start to False")
            CONFIG["auto-start"] = False
        else:
            self.auto_start_button.configure(image=self.ON_IMG)
            self.log.info(" Setting Auto-Start to True")
            CONFIG["auto-start"] = True

    def _count_down(self) -> None:
        """Start the countdown timer"""
        time_delta = 60000  # every minute
        if self.counter_is_active:
            self.counter_frame.update_display_counter(str(self.counter))  # Middle frame
            self.counter -= 1
            if self.counter < 0:
                # make alert
                if self.messagebox_is_active:
                    self.log.info("Activity box already active, skipping....")
                else:
                    self.messagebox_is_active = True
                    # Make the alert and reset active state
                    new_alert(audio_filename=CONFIG["default-audio"])  # Blocking call
                    self.messagebox_is_active = False
                # Reset Counter
                self.counter = int(CONFIG["interval"])
                self.counter_frame.update_display_counter(
                    str(self.counter)
                )  # Middle frame
            self.after(time_delta, self._count_down)


class CounterFrame(ctk.CTkFrame, CounterFrameMixin):
    def __init__(self, master, log):
        super().__init__(master, border_color="red", border_width=1)
        self.log = log
        self.intervals = [1] + list(
            range(10, 125, 5)
        )  # TODO remove after done testing.

        default_interval = ctk.StringVar(value=CONFIG["interval"])
        interval_option_menu = ctk.CTkOptionMenu(
            self,
            values=list(map(str, self.intervals)),
            command=self._set_interval,
            variable=default_interval,
            width=70,
        )
        interval_option_menu.grid(row=0, column=0)

        interval_unit_label = ctk.CTkLabel(self, text="minutes")
        interval_unit_label.grid(row=0, column=1)

        self.counter_display = ctk.CTkLabel(
            master=self,
            text=str(CONFIG["interval"]),
            font=("Helvetica", 70),
        )
        self.counter_display.grid(row=1, column=0, pady=10, columnspan=2)

    def _set_interval(self, choice) -> None:
        self.log.info(f" Setting interval to {choice}")
        CONFIG["interval"] = int(choice)
        self.update_display_counter(choice)

    def update_display_counter(self, value: str | int):
        value = str(value)
        self.counter_display.configure(text=value)


class OptionsFrame(ctk.CTkFrame):
    def __init__(self, master, log):
        super().__init__(master)
        self.log = log
        self.default_audio: str = CONFIG["default-audio"]

        update_button = ctk.CTkButton(master=self, text="Save", command=self._save)
        update_button.grid(row=2, column=0, pady=10, sticky="EW", columnspan=2)

        theme_option_label = ctk.CTkLabel(self, text="Theme")
        theme_option_label.grid(row=0, column=0, padx=2, pady=2)

        sound_option_label = ctk.CTkLabel(self, text="Alert Sound")
        sound_option_label.grid(row=1, column=0, padx=2, pady=2)

        theme_option_menu = ctk.CTkOptionMenu(
            self,
            values=["system", "dark", "light"],
            command=self._set_theme,
        )
        theme_option_menu.grid(row=0, column=1, padx=5, pady=2)

        default_audio = ctk.StringVar(value=CONFIG["default-audio"])
        sound_option_menu = ctk.CTkOptionMenu(
            self,
            values=self._load_audio_files(),
            command=self._set_audio,
            variable=default_audio,
        )
        sound_option_menu.grid(row=1, column=1, padx=5, pady=2)

    def _set_audio(self, audio_file_name) -> None:
        self.log.info(f"Updating audio config to {audio_file_name}")
        CONFIG["default-audio"] = audio_file_name

    def _set_theme(self, theme) -> None:
        self.log.info(f" changing theme to {theme}")
        ctk.set_appearance_mode(theme)

    def _save(self) -> None:
        """Update the configuration data."""
        self.log.info(" updating config...")
        update_config(CONFIG)

    def _load_audio_files(self) -> list[str]:
        """Load the audio files and create RadioButton selection(s)."""
        audio_assets_path = Path(__file__).parent.parent / "static/audio"
        if not audio_assets_path.exists():
            raise FileNotFoundError(
                f"Could not locate audio assets directory: {audio_assets_path}"
            )
        return [f.name for f in audio_assets_path.iterdir()]
