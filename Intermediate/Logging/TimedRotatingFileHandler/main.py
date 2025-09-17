import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create handler: rotates every 2 seconds, keeps 5 backups
handler = TimedRotatingFileHandler(
    'timed_test.log',
    when='s',           # Rotate based on seconds
    interval=2,         # Every 2 seconds
    backupCount=5       # Keep last 5 log files
)

# Add formatter
formatter = logging.Formatter('%m/%d/%Y %H:%M:%S - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Attach handler if not already added
if not logger.hasHandlers():
    logger.addHandler(handler)

# Log messages every 2 seconds
for i in range(3):
    logger.info(f'Hello, world! Message {i+1}')
    time.sleep(2)