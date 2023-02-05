import os
import requests
from telebot import types
from error_codes import *

async def getBalance(bot, message):
    
    api_url = os.getenv('APIURL')
    api_key = os.getenv('APIKEY')

    headers = {
                 "Authorization": f"API-KEY {api_key}",
                 'Content-Type': "application/json",
              }
    
    end_point = '/' + str(message.from_user.id)
    url = api_url + end_point
    response = requests.get (url, headers = headers)

    if (response.status_code == None):
        return await bot.send_message(message.from_user.id, "З’єднання із сервером тимчасово недоступне 😔\n"
                                                          + "Будь ласка, повторіть спробу пізніше.")
    try:
        response_data = response.json()
    except:
        await bot.send_message(message.from_user.id, "З’єднання із сервером тимчасово недоступне 😔\n"
                                                          + "Будь ласка, повторіть спробу пізніше!")
        return None
    
    if not (response.status_code == 200):
        if (response_data == None):
            await bot.send_message(message.from_user.id, error_codes(""))
            return None
        await bot.send_message(message.from_user.id, error_codes(response_data))
        return None
    return (response.json()['balance']) / 100


async def getPaymentData(bot, message):
    
    api_url = os.getenv('APIURL')
    api_key = os.getenv('APIKEY')

    headers = {
                 "Authorization": f"API-KEY {api_key}",
                 'Content-Type': "application/json",
              }
    
    end_point = '/' + str(message.from_user.id)
    url = api_url + end_point
    response = requests.get (url, headers = headers)
    
    if (response.status_code == None):
        return await bot.send_message(message.from_user.id, "З’єднання із сервером тимчасово недоступне 😔\n"
                                                          + "Будь ласка, повторіть спробу пізніше.")
    try:
        response_data = response.json()
    except:
        await bot.send_message(message.from_user.id, "З’єднання із сервером тимчасово недоступне 😔\n"
                                                          + "Будь ласка, повторіть спробу пізніше!")
        return None
    
    if not (response.status_code == 200):
        if (response_data == None):
            await bot.send_message(message.from_user.id, error_codes(""))
            return None
        await bot.send_message(message.from_user.id, error_codes(response_data))
        return None
    return {'id' : response.json()['_id'],
            'paymentLink' : response.json()['paymentLink']}
    
    
async def getSubscribes(bot, message):
    
    api_url = os.getenv('APIURL')
    api_key = os.getenv('APIKEY')

    headers = {
                 "Authorization": f"API-KEY {api_key}",
                 'Content-Type': "application/json",
              }
    
    end_point = '/' + str(message.from_user.id)
    url = api_url + end_point
    response = requests.get (url, headers = headers)
    
    if (response.status_code == None):
        return await bot.send_message(message.from_user.id, "З’єднання із сервером тимчасово недоступне 😔\n"
                                                          + "Будь ласка, повторіть спробу пізніше.")
    try:
        response_data = response.json()
    except:
        await bot.send_message(message.from_user.id, "З’єднання із сервером тимчасово недоступне 😔\n"
                                                          + "Будь ласка, повторіть спробу пізніше!")
        return None
    
    if not (response.status_code == 200):
        if (response_data == None):
            await bot.send_message(message.from_user.id, error_codes(""))
            return None
        await bot.send_message(message.from_user.id, error_codes(response_data))
        return None
    return (response.json()['subscriptions'])


async def getTransactions(bot, message):
    
    api_url = os.getenv('APIURL')
    api_key = os.getenv('APIKEY')

    headers = {
                 "Authorization": f"API-KEY {api_key}",
                 'Content-Type': "application/json",
              }
    
    end_point = '/' + str(message.from_user.id)
    url = api_url + end_point
    response = requests.get (url, headers = headers)
    
    if (response.status_code == None):
        return await bot.send_message(message.from_user.id, "З’єднання із сервером тимчасово недоступне 😔\n"
                                                          + "Будь ласка, повторіть спробу пізніше.")
    try:
        response_data = response.json()
    except:
        await bot.send_message(message.from_user.id, "З’єднання із сервером тимчасово недоступне 😔\n"
                                                          + "Будь ласка, повторіть спробу пізніше!")
        return None
    
    if not (response.status_code == 200):
        if (response_data == None):
            await bot.send_message(message.from_user.id, error_codes(""))
            return None
        await bot.send_message(message.from_user.id, error_codes(response_data))
        return None
    return (response.json()['transactions'])