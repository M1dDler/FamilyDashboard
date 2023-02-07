import os

async def support(bot, message):
    admin_id = os.getenv('ADMINID')
    
    if str(message.from_user.id) == str(admin_id):
        if not message.reply_to_message == None:
            try:
                return await bot.send_message(message.reply_to_message.forward_from.id, message.text)
            except:
                return await bot.send_message(admin_id, 'Можливо це не переслане повідомлення')
        return
    if not message.reply_to_message == None:
        await bot.send_message(admin_id, 'На запитання: \n' + message.reply_to_message.text + '\n від ' + message.from_user.first_name)
        return await bot.forward_message(admin_id, message.chat.id, message.id)
    return await bot.forward_message(admin_id, message.chat.id, message.id)