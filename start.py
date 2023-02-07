import asyncio
import os
from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot
from mainpage import *
from website import *
from balance import *
from subscribe import *
from transaction import *
from authorization import *
from unlinkTelegram import *
from mainpage import *
from support import *

load_dotenv()    
token = os.getenv('TOKEN')
bot = AsyncTeleBot(token)

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await authorization(bot, message)
    await mainpage(bot, message)


@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'voice', 'video_note'])
async def textMessage(message):
    if message.content_type == 'text':
    
        if message.text == "Веб-профіль 🖥":
            return await web_site(bot, message)
            
        if message.text == "Баланс коштів 💳":
            return await balance(bot, message)

        if message.text == "Мої підписки 📝":
            return await subscribe(bot, message)
            
        if message.text == "Мої транзакції 🔖":
            return await transaction(bot, message)
            
        if message.text == "Відв’язка Telegram 🔓":
            markup = types.InlineKeyboardMarkup()
            accept_unlinkTelegram = types.InlineKeyboardButton("1. Підтвердити ✅", callback_data = "accept unlinkTelegram")
            degree_unlinkTelegram = types.InlineKeyboardButton("2. Скасувати ❌", callback_data = "degree unlinkTelegram")
            markup.add(accept_unlinkTelegram, degree_unlinkTelegram)
            return await bot.send_message(message.from_user.id, "Ви дійсно бажаєте відв’язати свій аккаунт Telegram від веб-сайту? 🤔", reply_markup=markup)
        
        return await support(bot, message)
    return await support(bot, message)

@bot.callback_query_handler(func=lambda query: True)
async def balance_calldata(query):
        
    if (query.data == "show balance"):
        await show_balance(bot, query)
            
    if (query.data == "input balance"):
        await input_balance(bot, query)
    
    if (query.data == "accept unlinkTelegram"):
        await unlinkTelegram(bot, query)
        await bot.edit_message_reply_markup(query.from_user.id, query.json['message']['message_id'], reply_markup=None)
        
    if (query.data == "degree unlinkTelegram"):
        await bot.edit_message_reply_markup(query.from_user.id, query.json['message']['message_id'], reply_markup=None)

asyncio.run(bot.polling())