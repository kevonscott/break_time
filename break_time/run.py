################################################################################
# Application Name: BreakTime
# Author: Kevon Scott
# Description: A simple application to alert user to take mini-breaks
################################################################################

from __init__ import logger

from gui import BreakTime

if __name__ == "__main__":
    app = BreakTime()
    logger.info(" Launching app...")
    app.run()
