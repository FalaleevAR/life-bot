import os
import traceback

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types.input_file import InputFile

from bot.config import create_config, update_config, create_directory_if_not_exists
from bot.keyboards import configure_style_keyboard
from bot.keyboards import configure_count_keyboard, configure_intensity_keyboard
from bot import phrases

from log.logger import logger

from SmoothLife.smoothlife import save_animation

bot = Bot(token=os.environ['BOT_TOKEN'])
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message) -> None:
    logger.info(f'{message.from_user.id} said: {message.text}')
    try:
        chat_id = message.from_user.id
        create_config(chat_id)
        await message.answer(phrases.START_MSG, reply=False,
                             disable_notification=True)
        logger.info(f'{message.from_user.id}: replied with START_MSG')
    except Exception as e:
        logger.error(f'{message.from_user.id} said: {message.text} and caused {traceback.format_exc()}')
        raise RuntimeError from e


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message) -> None:
    logger.info(f'{message.from_user.id} said: {message.text}')
    try:
        await message.answer(phrases.HELP_MSG, reply=False,
                             disable_notification=True)
        logger.info(f'{message.from_user.id}: replied with START_MSG')
    except Exception as e:
        logger.error(f'{message.from_user.id} said: {message.text} and caused {traceback.format_exc()}')
        raise RuntimeError from e


@dp.message_handler(commands=['configure'])
async def send_configure(message: types.Message) -> None:
    logger.info(f'{message.from_user.id} said: {message.text}')
    try:
        await message.answer(phrases.CONFIGURE_BEFORE, reply=False, disable_notification=True, parse_mode='MARKDOWN')
        await message.answer(phrases.CONFIGURE_COUNT, reply=False, reply_markup=configure_count_keyboard,
                             disable_notification=True, parse_mode='MARKDOWN')
        await message.answer(phrases.CONFIGURE_INTENSITY, reply=False, reply_markup=configure_intensity_keyboard,
                             disable_notification=True, parse_mode='MARKDOWN')
        await message.answer(phrases.CONFIGURE_STYLE, reply=False, reply_markup=configure_style_keyboard,
                             disable_notification=True, parse_mode='MARKDOWN')
        await message.answer(phrases.CONFIGURE_AFTER, reply=False, disable_notification=True)
        logger.info(f'{message.from_user.id}: replied with INFO_MSG')
    except Exception as e:
        logger.error(f'{message.from_user.id} said: {message.text} and caused {traceback.format_exc()}')
        raise RuntimeError from e


@dp.callback_query_handler(lambda x: True)
async def process_callback(callback_query):
    chat_id = callback_query.from_user.id
    logger.info(f'{chat_id} said: {callback_query.data}')
    update_config(chat_id, callback_query.data)
    logger.info(f'{chat_id} changed: {callback_query.data}')
    await bot.answer_callback_query(callback_query.id)


@dp.message_handler(commands=['info'])
async def send_help(message: types.Message) -> None:
    logger.info(f'{message.from_user.id} said: {message.text}')
    try:
        await message.answer(phrases.INFO_MSG, reply=False, parse_mode='MARKDOWN',
                             disable_notification=True)
        logger.info(f'{message.from_user.id}: replied with INFO_MSG')
    except Exception as e:
        logger.error(f'{message.from_user.id} said: {message.text} and caused {traceback.format_exc()}')
        raise RuntimeError from e


@dp.message_handler(commands=['life'])
async def send_vid(message: types.Message) -> None:
    logger.info(f'{message.from_user.id} said: {message.text}')
    await message.answer(phrases.LIFE_TEXT_RESPONSE, reply=False,
                         disable_notification=True)
    logger.info(f'{message.from_user.id}: replied with life_text_response')
    chat_id = message.from_user.id
    directory = create_directory_if_not_exists(chat_id)
    path = os.path.join(directory, 'life.mp4')
    try:
        config = update_config(chat_id)
        save_animation(path, **config)
        await message.answer_video(InputFile(path), reply=False)
        logger.info(f'{message.from_user.id}: replied with animation')
    except Exception as e:
        logger.error(f'{message.from_user.id} said: {message.text} and caused {traceback.format_exc()}')
        raise RuntimeError from e


if __name__ == '__main__':
    executor.start_polling(dp)
