# coding=utf-8
import logging
import os,sys
sys.path.append("..")
from config import constants
def log_fun():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=os.path.join(constants.getPath("log_path"), 'log.txt'), level=logging.INFO)
    return logger

