import telebot
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from dataBase import getSubscribes

async def subscribe(bot, message):
    subscribes = await getSubscribes(bot, message)
    if subscribes == None or len(subscribes) == 0:
        return await bot.send_message(message.from_user.id, 'У вас відсутні активні підписки.')
    text = ""
        
    for sub in subscribes:
        text +=  ( "#️⃣ ID підписки: "+sub['_id']+"\n"
                +  "📝 Назва підписки: " +sub['title']+"\n" 
                +  "💰 Вартість підписки: " +str(sub['cost'] / 100)+ " грн/міс. \n")
    await bot.send_message(message.from_user.id, text)