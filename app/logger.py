

import logging
import os
import sys
import asyncio

from newrelic.api.log import NewRelicLogHandler

class TodoListLogger(logging.Logger):

  def _log(self, level, msg, args, exc_info=None, extra=None):
    if extra is None:
        extra = {}
<<<<<<< HEAD
    super(TodoListLogger, self)._log(level, msg, args, exc_info, extra)
=======
    extra['service'] = "todolist-app"
    super()._log(level, msg, args, exc_info, extra)


class AsyncNewRelicLogHandler(NewRelicLogHandler):

  def __init__(self, level):
    super().__init__(level=level, host="log-api.newrelic.com", license_key=os.getenv('NEW_RELIC_LICENSE_KEY'))
    # Create a new event loop to make sure tasks run in a separate loop
    self.loop = asyncio.new_event_loop()

  def emit(self, record):
    try:
      self.loop.create_task(self.async_emit(record))
    except Exception as e:
      super().emit(record)
    
  async def async_emit(self, record):
    super().emit(record)
>>>>>>> 5983227 (Async logging)

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

    # new_relic_handler = NewRelicLogHandler(level=level, host="log-api.newrelic.com", license_key=os.getenv('NEW_RELIC_LICENSE_KEY'))
    # logging.getLogger().addHandler(new_relic_handler)
    new_relic_handler = AsyncNewRelicLogHandler(level=level)
    logging.getLogger().addHandler(new_relic_handler)
<<<<<<< HEAD
    
    logger = logging.getLogger(__name__)        
    logger.debug("Logger initialized")
=======

    return new_relic_handler.loop
    # logger = logging.getLogger(__name__)        
    # logger.debug("Logger initialized")
>>>>>>> 5983227 (Async logging)
