import logging 
import os 
from logging.handlers import RotatingFileHandler

def setup_logging():
    logger = logging.getLogger(__name__)
    #set level
    logger.setLevel(logging.DEBUG)

    #Create a file handler 
    file_handler = RotatingFileHandler('app.log', maxBytes=1 * 1024 * 1024, backupCount=3)
    # file_handler.setLevel(logging.DEBUG)  # Set the level for the file handler
    
    #Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Set the level for the console handler

    #Create a formatter and set the format for the handlers
    formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)d - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info('Logging setup complete')
    return logger

if __name__ == "__main__":
    logger = setup_logging()
    for i in range(10):
        logger.info('info')
        logger.warning('warning')
        logger.error('error')
        logger.critical('critical')
        logger.debug('debug')