

import logging
import os
import sys

from newrelic.api.log import NewRelicLogHandler

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

    new_relic_handler = NewRelicLogHandler(level=level, host="log-api.newrelic.com", license_key=os.getenv('NEW_RELIC_LICENSE_KEY'))
    logging.getLogger().addHandler(new_relic_handler)
    
    logger = logging.getLogger(__name__)        
    logger.debug("Logger initialized")