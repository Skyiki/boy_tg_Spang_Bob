import telebot

token = '6682935044:AAEnE2y8KHraymUKeaxulz-4p0l5BWfcyhg'
bot = telebot.TeleBot(token=token)

function = ["start", "help", '']

function_description = {
    "start": "Начало работы бота",
    "help": "Справочная информация о доступных командах и их функциональности."
}

def functions():
    for i in range(len(function_description)):
        print(i + 1, '-', function_description[i])


@bot.message_handler(commands=['start'])
def start_func(message):
    bot.send_message(chat_id=message.chat.id, text= f'Это бот визитка для известного персонажа - Губку Боба! \n'
                                                    f'Можешь ознакомиться с доступными командами с помощью команды /help'
                     )

@bot.message_handler(commands=['help'])
def help_func(message):
    bot.send_message(chat_id=message.chat.id, text= f'У этого бота присутвуют команды: {function_description}')

bot.infinity_polling()
