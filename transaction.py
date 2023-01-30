import telebot
import datetime
import os
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from dataBase import getTransactions

async def transaction(bot, message):
    transactionUrl = os.getenv('SITEURL')
    transactionUrl += 'transactions' 
    transactions = await getTransactions(bot, message)
    if transactions == None or len(transactions) == 0:
        return await bot.send_message(message.from_user.id, 'У вас відсутні транзакції')
    markup = types.InlineKeyboardMarkup()
    transactions_btn = types.InlineKeyboardButton("Переглянути повний список транзакцій", url = transactionUrl)
    markup.add(transactions_btn)
    
    text = ("")
            
    for trans in transactions:
        input = trans['date']
        format = ('%Y-%m-%dT%H:%M:%S.%f%z')
        date = datetime.datetime.strptime(input, format).strftime('%d.%m.%Y %H:%M:%S')
        
        text += ( "#️⃣ ID транзакції: " +str(trans['_id'])+ "\n"
                + "📝 Опис транзакції: " +str(trans['title'])+ "\n" 
                + "💰 Сума транзакції: " +str(trans['suma'] / 100) + " грн.\n"
                + "📅 Дата транзакції: " +str(date)+ "\n\n\n")
    
    await bot.send_message(message.from_user.id, text, reply_markup=markup)