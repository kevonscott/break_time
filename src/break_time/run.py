################################################################################
# Application Name: BreakTime
# Author: Kevon Scott
# Description: A simple application to alert user to take mini-breaks
################################################################################


from __init__ import logger
from utils.gui import BreakTime

if __name__ == "__main__":
    logger.info(" Launching BreakTime...")
    breaktime = BreakTime(log=logger)
    breaktime.run()
