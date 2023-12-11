import telebot
import random

from telebot import types

token = '6682935044:AAEnE2y8KHraymUKeaxulz-4p0l5BWfcyhg'
bot = telebot.TeleBot(token=token)

function = ["start", "help", 'hobby', 'aboutme', 'job', "question"]

function_description = {
    "start": "Начало работы бота",
    "help": "Справочная информация о доступных командах и их функциональности.",
    "hobby": "Рассказывает про свои увлечения, работу, хобби.",
    "aboutme": "Рассказывает про себя.",
    "job": "Рассказывает про работу.",
    "question": "Показывает список на что может ответить бот."
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
                                                   f"/start - Запуск бота. \n"
                                                   f"/help - Справочная информация о доступных командах и их "
                                                   f"функциональности. \n"
                                                   f"/hobby - Рассказывает про свои увлечения, работу, хобби. \n"
                                                   f"/aboutme - Рассказывает про себя. \n"
                                                   f"/job - Рассказывает про работу. \n"
                                                   f"/question - Показывает список на что может ответить бот."
                     )


@bot.message_handler(commands=['hobby'])
def help_func(message):
    bot.send_message(chat_id=message.chat.id,
                     text=f'Мне нравится в свободное время ловить медуз с моим другом Патриком.'
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

@bot.message_handler(commands=['question'])
def question_func(message):
    bot.send_message(chat_id=message.chat.id, text=f"На что может ответить бот: \n"
                                                   f"1 - Привет \n"
                                                   f"2 - Пока \n"
                                                   f"3 - Как дела? \n"
                                                   f"4 - Кто твой друг?| Есть друзья? \n"
                                                   f"5 - Кого любишь ловить со своим другом? \n"
                                                   f"6 - Откуда ты?| Где живёшь? \n"
                                                   f"7 - Сколько у тебя ресниц? \n"
                                                   f"8 - Какого цвета глаза? \n"
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
def bue(message):
    bot.send_message(chat_id=message.chat.id, text='До скорой встречи! Боб никогда не забудет вас.')

#список ответов
how_are_you = ['Отлично! Иду с Патриком ловить медуз!', "Отлично, возвращаюсь домой из Красти Краба.",
               "Медузительно! Поймал несколько медуз сегодня!"]
#random_index = random.randrange(len(how_are_you)) один из вариантов кода
how_ares_you = random.choice(how_are_you)

def howareyou(message):
    msg = "как дела"
    return msg in message.text.lower()


@bot.message_handler(content_types=['text'], func=howareyou)
def howareyou_func(message):
    bot.send_message(chat_id=message.chat.id, text=f'{how_ares_you}')


#тоже список ответов
best_friend = ["У меня много друзей: Патрик, Скидвард, Мистер Крабс, Сенди и много кто ещё!", "Мой лучший друг - Гэри!"]
best_friends = random.choice(best_friend)
def bestfriend(message):
    msg = "кто твой друг"
    return msg in message.text.lower()


@bot.message_handler(content_types=['text'], func=bestfriend)
def bestfriend(message):
    bot.send_message(chat_id=message.chat.id, text=best_friends)


def bestfriendу(message):
    msg = "есть друзья"
    return msg in message.text.lower()


@bot.message_handler(content_types=['text'], func=bestfriendу)
def bestfriendу(message):
    bot.send_message(chat_id=message.chat.id, text=best_friends)


def jellyfish(message):
    msg = "кого любишь ловить"
    return msg in message.text.lower()


@bot.message_handler(content_types=['text'], func=jellyfish)
def jellyfish(message):
    bot.send_message(chat_id=message.chat.id, text='Я обожаю ловить медуз с моим лучшим другом - Патриком!')


def home(message):
    msg = "откуда ты"
    return msg in message.text.lower()
@bot.message_handler(content_types=['text'], func=home)
def home(message):
    bot.send_message(chat_id=message.chat.id, text='Я живу в прекрасном подводном городе Бикини Боттом!')



def homes(message):
    msg = "где живёшь"
    return msg in message.text.lower()

@bot.message_handler(content_types=['text'], func=homes)
def homes(message):
    bot.send_message(chat_id=message.chat.id, text='Я живу своём доме-ананасе на окраине Бикини Боттом!')



def eyess(message):
    msg = "сколько у тебя ресниц"
    return msg in message.text.lower()

@bot.message_handler(content_types=['text'], func=eyess)
def eyess(message):
    bot.send_message(chat_id=message.chat.id, text='Трудная задачка их посчитать, но я думаю их пять!')



def eyes(message):
    msg = "какого цвета глаза"
    return msg in message.text.lower()


@bot.message_handler(content_types=['text'], func=eyes)
def eyes(message):
    bot.send_message(chat_id=message.chat.id, text='Мои глаза? Они похожи на воду! Такие же голубые.')


bot.infinity_polling()
