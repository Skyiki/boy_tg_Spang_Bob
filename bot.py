import telebot

token = '6682935044:AAEnE2y8KHraymUKeaxulz-4p0l5BWfcyhg'
bot = telebot.TeleBot(token=token)

function = ["start", "help", 'hobby', 'aboutme']

function_description = {
    "start": "Начало работы бота",
    "help": "Справочная информация о доступных командах и их функциональности.",
    "hobby": "Рассказывает про свои увлечения, работу, хобби.",
    "aboutme": "Рассказывает про себя."
}


# def functions():
#    for i in range(len(function_description)):
#        pp = pprint.PrettyPrinter(indent=2)
#        pp.pprint(function_description)


@bot.message_handler(commands=['start'])
def start_func(message):
    bot.send_message(chat_id=message.chat.id,
                     text=f'В Бикини Боттом новый день, и я, Губка Боб, здесь, чтобы сделать его особенным! \n'
                          f'Хочешь узнать, что я могу? Тогда нажимай - /help'
                     )


@bot.message_handler(commands=['help'])
def help_func(message):
    bot.send_message(chat_id=message.chat.id, text=f"Я умею: \n"
                                                   f"/start - запуск бота. \n"
                                                   f"/help - справочная информация о доступных командах и их "
                                                   f"функциональности. \n"
                                                   f"/hobby - рассказывает про свои увлечения, работу, хобби. \n"
                                                   f"/aboutme - рассказывает про себя. \n"
                     )


@bot.message_handler(commands=['hobby'])
def help_func(message):
    bot.send_message(chat_id=message.chat.id, text=f'Мне нравится в свободное время ловить медуз с моим другом Патриком.'
                                                   f' Это наше общее хобби, которое мы оба очень любим.'
                                                   f' Мы проводим много времени на пляже, пытаясь поймать как '
                                                   f'можно больше медуз.\n'
                                                   f'Иногда мы даже соревнуемся друг с другом, кто поймает '
                                                   f'больше медуз за определенное время!')

@bot.message_handler(commands=['aboutme'])
def aboutme_func(message):
    bot.send_message(chat_id=message.chat.id, text=f'Моя жизнь полна приключений, забавных ситуаций и самых верных '
                                                   f'друзей!'
                                                   f' Мой лучший друг - это, конечно же, Патрик Стар, глуповатый, '
                                                   f'но невероятно милый и забавный звезда.'
                                                   f' А еще у меня есть Сквидвард, сосед и коллега по работе, который '
                                                   f'постоянно ворчит и ругает меня, но на самом деле он очень добрый '
                                                   f'и заботливый.'
                                                   f' Я люблю свою работу и свой город, и каждый день я узнаю что-то '
                                                   f'новое и интересное. Бикини Боттом - это место, где возможно все, '
                                                   f'и я всегда готов к новым приключениям и безумным выходкам!')

@bot.message_handler(commands=['job'])
def job_func(message):
    bot.send_message(chat_id=message.chat.id, text=f'Я работаю в Красти Краб, лучшем ресторане на свете, где я '
                                                   f'готовлю вкуснейшие крабсбургеры для своих любимых клиентов.'
                                                   f' Я обожаю свою работу!'
    )
def hello(message):
    msg = 'привет'
    return msg in message.text.lower()

@bot.message_handler(content_types=['text'], func=hello)
def hello_func(message):
    bot.send_message(chat_id=message.chat.id, text='Привет! Сегодня будет незабываемый день в Бикини Боттом!')

def bue(message):
    msg = "пока"
    return msg in message.text.lower()

@bot.message_handler(content_types=['text'], func=bue)
def hello_func(message):
    bot.send_message(chat_id=message.chat.id, text='До скорой встречи! Боб никогда не забудет вас.')

def (message):
    msg = "пока"
    return msg in message.text.lower()

@bot.message_handler(content_types=['text'], func=bue)
def hello_func(message):
    bot.send_message(chat_id=message.chat.id, text='До скорой встречи! Боб никогда не забудет вас.')

def bue(message):
    msg = "пока"
    return msg in message.text.lower()

@bot.message_handler(content_types=['text'], func=bue)
def hello_func(message):
    bot.send_message(chat_id=message.chat.id, text='До скорой встречи! Боб никогда не забудет вас.')

def bue(message):
    msg = "пока"
    return msg in message.text.lower()

@bot.message_handler(content_types=['text'], func=bue)
def hello_func(message):
    bot.send_message(chat_id=message.chat.id, text='До скорой встречи! Боб никогда не забудет вас.')


bot.infinity_polling()