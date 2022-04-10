import logging
import os
import sys

def init_logger():
    logging.getLogger().setLevel(logging.NOTSET)
    LOG_FORMAT = ("%(levelname) -10s %(asctime)s %(name) "
                "-30s %(funcName) -35s %(lineno) -5d: %(message)s")
    level = os.environ.get('LOG_LEVEL', 'INFO')
    formatter = logging.Formatter(LOG_FORMAT)
    
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logging.getLogger().addHandler(ch)
    logger = logging.getLogger(__name__)        
    logger.debug("Logger initialized")
