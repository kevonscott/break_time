import random

from __init__ import logger
from config.config import ACTIVITIES, REP_COUNT
from message_box import MessageBox
from sound.sound import Sound


def new_alert(audio_filename):
    logger.info("Randomly selecting break Activity and Duration or Rep...")
    random_reps = random.choice(REP_COUNT)  # Choose a random number of reps/munutes
    random_activity_type = random.choice(list(ACTIVITIES.keys()))
    random_activity = random.choice(ACTIVITIES[random_activity_type][0])
    rep_unit = ACTIVITIES[random_activity_type][1]
    logger.info(f"\n Activity: {random_activity} \n Duration or Rep: {random_reps}")
    message = f"{random_reps} {rep_unit} {random_activity}"
    subject = "Take a short break!!!"

    logger.info("Playing sound to alert user....")
    sound_object = Sound(filename=audio_filename)
    sound_object.play()

    logger.info("Launching Display Box and waiting for user response...")
    message_box = MessageBox(message=message, subject=subject)
    message_box.display()
    logger.info("Completed successfully...")
