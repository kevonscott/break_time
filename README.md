# BREAK_TIME

break_time is a simple program designed for **Windows OS** to run as a job in
Task Scheduler to alert a user to take occasional breaks while working. 
break_time randomly chooses from a set of predefined activities, reps or duration 
from the config/config.yml configuration file and recommend to the user in the 
form of a display box. To add more activities would be as simple as appending to
 the yaml configuration. An mp3 audio from data/sound is also played along with 
the message box so the user gets both audio and visual notification. 

This program was inspired by 
[stop_sitting](https://github.com/custerc/stop_sitting "stop_sitting")

## Future Improvements

* Create a full GUI for user configuration
* Make sound option configurable
* Build app into exe so it can be installed like other programs
* Create Linux/Unix version of the application
