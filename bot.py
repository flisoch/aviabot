import datetime

import telebot
from telebot import types

TOKEN = '587528180:AAG4hsUKfoguxfkSEeyTzrD65PMKuy3EPbU'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(msgt):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Меню"))
    greeting = 'Этот бот поможет вам узнать цены на рейсы по выбранным вами направлениям перелёта\n' \
               'Доступные команды:\n/calc - подсчитает стоимость перелёта\n' \
               '/help - помощь по командам бота\n' \
               '/menu - меню бота'

    bot.send_message(msgt.chat.id, greeting, reply_markup=keyboard)


@bot.message_handler(regexp='(М|м)еню')
def extra_menu(msg):
    menu(msg)


@bot.message_handler(regexp='(К|к)алькулятор')
def extra_cals(msg):
    calc(msg)


@bot.message_handler(regexp='Помощь')
def extra_help(message):
    help(message)


@bot.message_handler(regexp='Наш Сайт')
def site(msg):
    date = str(datetime.datetime.now()).split()[0]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Перейти на сайт',
                                            url='https://www.uzairways.com/ru/tariffcalc?currency=UZS&'
                                                'tablofrom=TAS&tabloto=IST&'
                                                'date=' + date))  # сайт кнопка-ссылка
    bot.send_message(msg.chat.id, "Чтобы перейти на наш сайт, нажмите кнопку ниже", reply_markup=keyboard)


# def menu_func(msg):
#     # message = bot.get_updates(msg.chat.id)
#     msgText = msg.text
#
#     if msgText == "Помощь" or msg.text == "/help":
#         help(msg)
#     elif msgText == "Калькулятор" or msg.text == "/calc":
#         calc(msg)
#     elif msgText == "Наш сайт":
#         keyboard = types.InlineKeyboardMarkup()
#         keyboard.add(types.InlineKeyboardButton(text='Перейти на сайт', url='ya.ru'))  # сайт кнопка-ссылка
#         bot.send_message(msg.chat.id, "Чтобы перейти на наш сайт, нажмите кнопку ниже", reply_markup=keyboard)
#     elif msgText == "/menu" or msg.text == "Меню":
#         bot.send_message(msg.chat.id, "Неизвестная команда")
#         menu(msg)


@bot.message_handler(commands=['menu'])
def menu(msg):
    # toDO: написать функцию, которая в зависимости от выбр кнопки вызывает команду.

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.add(*[types.KeyboardButton(name) for name in ['Калькулятор', 'Помощь']])
    keyboard.add(types.KeyboardButton("Наш сайт"))

    msg = bot.send_message(msg.chat.id, 'Нажмите на одну из кнопок или наберите одну из доступных команд'
                                        '\nСписок всех команд доступен в разделе "Помощь"', reply_markup=keyboard)
    print("msg from: " + msg.chat)
    # bot.register_next_step_handler(message=msg, callback=menu_func(msg))


@bot.message_handler(commands=['help'])
def help(message):
    detailedCommandsInfo = ' Доступные команды бота:\n\n' \
                           '/calc введите то сё(описание всех шагов)\n\n' \
                           '/menu вызовет меню бота, откуда можно работать без вызова команд\n\n' \
                           '/help - помощь по использованию бота\n\n' \
                           'На наш сайт можно выйти из Меню\n\n'

    bot.send_message(message.chat.id, detailedCommandsInfo)


@bot.message_handler(commands=['calc'])  # калькулятор можно в отдельный класс и все функции там прописать
def calc(m):
    instruction = '1. bla bla \n 2.bla bla ... 4-5'

    bot.send_message(m.chat.id, instruction)
    # bot.register_next_step_handler(msg, name)


bot.polling(none_stop=True)
