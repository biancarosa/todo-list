

import logging
import os
import sys


class TodoListLogger(logging.Logger):

  def _log(self, level, msg, args, exc_info=None, extra=None):
    if extra is None:
        extra = {}
    super(TodoListLogger, self)._log(level, msg, args, exc_info, extra)

def init_logger():
    logging.setLoggerClass(TodoListLogger)
    logging.getLogger().setLevel(logging.NOTSET)
    level = logging.getLevelName(os.environ.get('LOG_LEVEL', 'INFO'))


    LOG_FORMAT = ("%(levelname) -10s %(asctime)s %(name) "
                "-30s %(funcName) -35s %(lineno) -5d: %(message)s")
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(LOG_FORMAT)
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logging.getLogger().addHandler(ch)


    logger = logging.getLogger(__name__)        
    logger.debug("Logger initialized")