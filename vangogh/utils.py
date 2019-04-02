import logging.handlers

logger = logging.getLogger("vangogh")
formatter = logging.Formatter('%(asctime)s : %(filename)s : %(funcName)s : %(lineno)s : %(levelname)s : %(message)s')
fileMaxByte = 256 * 1024 * 200  # 100MB
consoleHandler = logging.StreamHandler()
fileHandler = logging.handlers.RotatingFileHandler('./logs/vangogh.log', maxBytes=fileMaxByte, backupCount=10)
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)
logger.setLevel(logging.INFO)
