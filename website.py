import telebot
import os
from telebot import types
from telebot.async_telebot import AsyncTeleBot

async def web_site(bot, message):
    siteUrl = os.getenv('SITEURL')
    markup = types.InlineKeyboardMarkup()
    site_btn = types.InlineKeyboardButton("Перейти на сайт профілю 🌐", url = siteUrl)
    markup.add(site_btn)
    await bot.send_message(message.from_user.id, "Для перегляду даних профілю перейдіть за посиланням нижче.", reply_markup=markup)
    