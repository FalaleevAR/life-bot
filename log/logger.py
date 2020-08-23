import os
import logging
from logging.handlers import TimedRotatingFileHandler

from telegram_handler import TelegramHandler

from bot.settings import ADMIN_CHAT_ID

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler = TimedRotatingFileHandler('log/info.log', when='d', interval=7, backupCount=10)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

telegram_handler = TelegramHandler(os.environ['BOT_TOKEN'], ADMIN_CHAT_ID, level=logging.WARNING)
telegram_handler.setFormatter(formatter)
logger.addHandler(telegram_handler)
