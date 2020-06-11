#-------------------------------------------------------------------------------
# Python Module to log to Console and File
#-------------------------------------------------------------------------------
import logging

#Start the Logger
logger = logging.getLogger()

#Set the logging level
logger.setLevel(logging.DEBUG)

#Start Screen Logging Handler
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#Start File Logging Handler
handler = logging.FileHandler('log.log')
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
