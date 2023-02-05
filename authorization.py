import os
import requests
from telebot import types
from error_codes import *

async def authorization (bot, message):
    key = message.json['text'].split(" ")
    if not len(key) == 2:
        return
    
    api_url = os.getenv('APIURL')
    api_key = os.getenv('APIKEY')
    
    headers = {
                "Authorization": f"API-KEY {api_key}",
                'Content-Type': "application/json",
            }
    
    body = {
            "telegramID": message.from_user.id,
            "key": key[1]
        }
    
    response = requests.post(api_url, headers = headers, json = body)
    

    if (response.status_code == None):
        return await bot.send_message(message.from_user.id, "З’єднання із сервером тимчасово недоступне 😔\n"
                                                          + "Будь ласка, повторіть спробу пізніше.")
    try:
        response_data = response.json()
    except:
        return await bot.send_message(message.from_user.id, "З’єднання із сервером тимчасово недоступне 😔\n"
                                                          + "Будь ласка, повторіть спробу пізніше!")
        
    if not (response.status_code == 200):
        if (response_data == None):
            return await bot.send_message(message.from_user.id, error_codes(""))
        return await bot.send_message(message.from_user.id, error_codes(response_data))
    siteUrl = os.getenv('SITEURL')
    markup = types.InlineKeyboardMarkup()
    linked_btn = types.InlineKeyboardButton("Перейти до веб-профілю 🌐", url = siteUrl)
    markup.add(linked_btn)
    await bot.send_message(message.from_user.id, "Ваш аккаунт Telegram успішно зв’язано із веб-сайтом! 🥳", reply_markup=markup)       
        