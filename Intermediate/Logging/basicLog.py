import logging

logger = logging.getLogger(__name__)

# create handler
streamH = logging.StreamHandler()
fileH = logging.FileHandler('file.log')

# level and the format
streamH.setLevel(logging.WARNING)
fileH.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
streamH.setFormatter(formatter)
fileH.setFormatter(formatter)

logger.addHandler(streamH)
logger.addHandler(fileH)

logger.warning('this is a warning')
logger.error('this is an error')