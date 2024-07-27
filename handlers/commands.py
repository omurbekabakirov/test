import glob
import random
import os
from aiogram.types import InputFile
from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup


async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Привет! {message.from_user.first_name}\n\n'
                                f'Твой tg id -- {message.from_user.id}')


async def info(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Я могу принять заказ')


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(info, commands=['info'])
