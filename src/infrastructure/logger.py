import logging

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

def info(data):
  _logger.info(data)