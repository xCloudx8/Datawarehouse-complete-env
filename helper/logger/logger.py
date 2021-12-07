import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

log_name = "log_"+(datetime.today()).strftime('%Y%m%d')
logPath = 'helper/logger/logs/'
file = logPath+log_name

logger=logging.getLogger() 

os.makedirs(os.path.dirname(file), exist_ok=True)

def info(msg):
    logging.basicConfig(
        handlers=[RotatingFileHandler(file, maxBytes=100000, backupCount=10)],
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S')
    logger.info(msg)

def warn(msg):
    logging.basicConfig(
        handlers=[RotatingFileHandler(file, maxBytes=100000, backupCount=10)],
        level=logging.WARNING,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S')
    logger.warning(msg)

def crit(msg):
    logging.basicConfig(
        handlers=[RotatingFileHandler(file, maxBytes=100000, backupCount=10)],
        level=logging.CRITICAL,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S')
    logger.critical(msg)