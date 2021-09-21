import logging
import sys
from logging.handlers import TimedRotatingFileHandler
from os import mkdir
from os.path import exists, join

from src.helpers.util import get_config_key
from src.settings import LOG_PATH


def log_config():
    if not exists(LOG_PATH):
        mkdir(LOG_PATH)

    formatter = '%(asctime)s  [%(name)s - %(levelname)s] >> %(message)s'

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(logging.Formatter(formatter))

    log_name = join(LOG_PATH, f'{get_config_key("app_name")}_{get_config_key("version")}.log')
    file_handler = TimedRotatingFileHandler(log_name, when="midnight", interval=1)
    file_handler.suffix = "%Y%m%d"

    logging.basicConfig(format=formatter.replace('%(asctime)s', '%(asctime)s.%(msecs)03d'), datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG, handlers=[file_handler, stdout_handler])
