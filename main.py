import telebot

token = '6682935044:AAEnE2y8KHraymUKeaxulz-4p0l5BWfcyhg'
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start_func(message):
    bot.send_message(chat_id=message.chat.id, text= f'Это бот визитка для всем известного персонажа - Губку Боба! \n'
                                                    f'Можешь ознакомиться с доступными командами с помощью команды /help'
                     )

def help