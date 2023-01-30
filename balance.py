import telebot
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from dataBase import getBalance, getPaymentData

async def balance(bot, message):
    markup2 = types.InlineKeyboardMarkup()
    show_balance_btn = types.InlineKeyboardButton("1. Показати баланс 📤", callback_data = "show balance")
    input_balance_btn = types.InlineKeyboardButton("2. Поповнити баланс 📲", callback_data = "input balance")
    markup2.add(show_balance_btn, input_balance_btn)
    await bot.send_message(message.from_user.id, "Оберіть одну із можливих операцій ⤵️:", reply_markup=markup2)


async def show_balance(bot, query):
    balance = await getBalance(bot, query)
    if balance == None:
        return
    await bot.send_message(query.from_user.id, "Ваш поточний баланс - "+str(balance)+" грн. 💼")
    
    
async def input_balance(bot, query):
    payment_data = await getPaymentData(bot, query)
    if payment_data == None:
        return
    if payment_data['paymentLink'] == "":
       return await bot.send_message(query.from_user.id, "Зверніться до адміністрації для налаштування платіжних даних 📲")
    markup = types.InlineKeyboardMarkup()
    monobanka_btn = types.InlineKeyboardButton("Поповнити рахунок 💵", url = payment_data['paymentLink'])
    markup.add(monobanka_btn)
    await bot.send_message(query.from_user.id, "Поповнити баланс можливо, переказавши кошти в банку Monobank, натиснувши відповідну кнопку нижче. ⤵️\n\n"
                     + "Обов’язково❗️ В коментарі платежу вкажіть ваш ID: - "+str(payment_data['id']), reply_markup=markup)