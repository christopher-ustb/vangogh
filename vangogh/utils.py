import logging.handlers
import os

from vangogh import settings


def _get_logger():
    vangogh_logger = logging.getLogger("vangogh")
    formatter = logging.Formatter(
        '%(asctime)s : %(threadName)s : %(filename)s : %(funcName)s : %(lineno)s : %(levelname)s : %(message)s')
    file_max_byte = 256 * 1024 * 200  # 100MB
    console_handler = logging.StreamHandler()
    os.makedirs(os.path.dirname(settings.LOGGER_FILE), exist_ok=True)
    file_handler = logging.handlers.RotatingFileHandler(settings.LOGGER_FILE, maxBytes=file_max_byte, backupCount=10)
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    vangogh_logger.addHandler(console_handler)
    vangogh_logger.addHandler(file_handler)
    vangogh_logger.setLevel(logging.INFO)
    return vangogh_logger


def absolute_path_to_server_url(absolute_path):
    basic_dir_length = len(settings.PHOTO_BASIC_DIR)
    return absolute_path[basic_dir_length:].replace("\\", "/")


def server_url_to_absolute_path(server_url):
    return os.path.join(settings.PHOTO_BASIC_DIR, *server_url.split("/"))


logger = _get_logger()
