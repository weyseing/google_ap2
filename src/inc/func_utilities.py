import logging
import colorlog

# setup logger
def setup_colored_logging(level=logging.INFO):
    LOG_FORMAT = (
        '%(log_color)s%(asctime)s - '
        '%(levelname)-8s - '  # The '-8s' ensures the level name is always 8 chars wide for alignment
        '%(message)s'
    )
    
    formatter = colorlog.ColoredFormatter(
        LOG_FORMAT,
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'bold_red,bg_white',
        }
    )
    
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    
    if root_logger.hasHandlers():
        root_logger.handlers.clear()
        
    root_logger.addHandler(stream_handler)

# init logger
setup_colored_logging(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_info(msg):
    logger.info(msg)

def log_error(msg):
    logger.error(msg)

def log_debug(msg):
    logger.debug(msg)