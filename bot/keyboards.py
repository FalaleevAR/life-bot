from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from bot.settings import CONFIGURE


def fill_inline_keyboard(key, keyboard):
    button_list = []
    for item in CONFIGURE[key]:
        if isinstance(item, str):
            button_list.append(InlineKeyboardButton(f'{item}', callback_data=f'dict({key}="{item}")'))
        else:
            button_list.append(InlineKeyboardButton(f'{item}', callback_data=f'dict({key}={item})'))
    keyboard.add(*button_list)


keyboard_reply = ReplyKeyboardMarkup([['/life'], ['/info']])

configure_count_keyboard = InlineKeyboardMarkup()
fill_inline_keyboard('count', configure_count_keyboard)

configure_intensity_keyboard = InlineKeyboardMarkup()
fill_inline_keyboard('intensity', configure_intensity_keyboard)

configure_style_keyboard = InlineKeyboardMarkup()
fill_inline_keyboard('style', configure_style_keyboard)
