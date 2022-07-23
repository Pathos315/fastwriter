r"""Sets up the logger as a stream for the program.
    """
    
import logging

logger = logging.getLogger("fastwriter")
logger.setLevel(level=logging.INFO)
datefmt = "%y-%m-%d %H:%M:%S"
formatter = logging.Formatter("\n[fastwriter]: %(asctime)s - %(message)s\n")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)