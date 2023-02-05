import os
import requests
from telebot import types
from error_codes import *

async def unlinkTelegram (bot, query):
    api_url = os.getenv('APIURL')
    api_key = os.getenv('APIKEY')
    
    headers = {
                "Authorization": f"API-KEY {api_key}",
                'Content-Type': "application/json",
            }
    
    body = {
            "telegramID": query.from_user.id
        }
    
    response = requests.delete(api_url, headers = headers, json = body)
    
    if (response.status_code == None):
        return await bot.send_message(query.from_user.id, "З’єднання із сервером тимчасово недоступне 😔\n"
                                                          + "Будь ласка, повторіть спробу пізніше.")
    try:
        response_data = response.json()
    except:
        return await bot.send_message(query.from_user.id, "З’єднання із сервером тимчасово недоступне 😔\n"
                                                          + "Будь ласка, повторіть спробу пізніше!")
        
    if not (response.status_code == 200):
        if (response_data == None):
            return await bot.send_message(query.from_user.id, error_codes(""))
        return await bot.send_message(query.from_user.id, error_codes(response_data))
    await bot.send_message(query.from_user.id, "Ваш аккаунт Telegram успішно відв’язано від веб-сайту! 🥳")   
    
    