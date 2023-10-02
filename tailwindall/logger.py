import os, sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import logging

logger = logging.getLogger(__name__)

def info(text):
    logger.info(text)

def debug(text):
    logger.debug(text)

def warning(text):
    logger.warning(text)

def error(text):
    logger.error(text)
