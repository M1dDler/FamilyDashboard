import telebot
from telebot import types
from telebot.async_telebot import AsyncTeleBot

async def mainpage(bot, message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
    balance_btn = types.KeyboardButton("Баланс коштів 💳")
    subscribe_btn = types.KeyboardButton("Мої підписки 📝")
    transaction_btn = types.KeyboardButton("Мої транзакції 🔖")
    site_btn = types.KeyboardButton("Веб-профіль 🖥")
    unlinkTelegram_btn = types.KeyboardButton("Відв’язка Telegram 🔓")
    markup.add(site_btn, subscribe_btn, balance_btn, transaction_btn, unlinkTelegram_btn)
    await bot.send_message(message.from_user.id, "Оберіть те, що вас цікавить! 😇", reply_markup=markup)