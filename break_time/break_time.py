################################################################################
# Application Name: Break Time
# Author: Kevon Scott
# VersionL 1.0
# Description: A simple application to alert user to take mini-breaks
################################################################################

import random
from message_box import MessageBox
from sound import Sound
from config.config import ACTIVITIES, REP_COUNT, ALERT_FILE
import logging

logging.basicConfig(level=logging.INFO)

def main():
    logging.info('Randomly selecting break Activity and Duration\Rep...')
    random_reps = random.choice(REP_COUNT) # Choose a random number of reps/munutes
    random_activity_type = random.choice(list(ACTIVITIES.keys()))
    random_activity = random.choice(ACTIVITIES[random_activity_type][0])
    rep_unit = ACTIVITIES[random_activity_type][1]
    logging.info(f'\n Activity: {random_activity} \n Duration\Rep: {random_reps}')
    message = f'{random_reps} {rep_unit} {random_activity}'
    subject = 'Take a short break!!!'
    
    logging.info('Playing sound to alert user....')
    sound_object = Sound(filename=ALERT_FILE)
    sound_object.play()
    
    logging.info('Launching Display Box and waiting for user response...')
    message_box = MessageBox(message=message, subject=subject)
    message_box.display()
    logging.info('Completed successfully, exiting...')
  
if __name__=='__main__':
    main()