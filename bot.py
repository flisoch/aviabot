import telebot
from telebot import types

TOKEN = '587528180:AAG4hsUKfoguxfkSEeyTzrD65PMKuy3EPbU'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(msgt):

    #toDo: связать с командой Меню 
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Меню"))
    greeting = 'Это бот блаблабла\n коротко о командах: бла бла бла'
    bot.send_message(msgt.chat.id, greeting,reply_markup=keyboard)

    # bot.register_next_step_handler(msg, name)
    # menu(msgt)

@bot.message_handler(regexp='Меню')
def extra_menu(msg):
    menu(msg)

@bot.message_handler(commands=['menu'])
def menu(msg):

    #toDO: написать функцию, которая в зависимости от выбр кнопки вызывает команду. 

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Наш сайт',url='ya.ru'))     #сайт кнопка-ссылка

    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1.add(*[types.KeyboardButton(name) for name in ['Калькулятор','Помощь']])

    bot.send_message(msg.chat.id,'нащ',reply_markup=keyboard1)
    bot.send_message(msg.chat.id,'сайт',reply_markup=keyboard)


@bot.message_handler(regexp='Помощь')
def extra_help(message):
    help(message)

@bot.message_handler(commands=['help'])
def help(message):

    #Todo: обеспечить меню после хелп-текста

    detailedCommandsInfo = ' /calc is bla bla /menu is bla bla bla /help is bla'

    bot.send_message(message.chat.id, detailedCommandsInfo)


@bot.message_handler(commands=['calc'])                             #калькулятор можно в отдельный класс и все функции там прописать
def calc(m):

    instruction = '1. bla bla \n 2.bla bla ... 4-5'

    bot.send_message(m.chat.id, instruction)

    # bot.register_next_step_handler(msg, name)


bot.polling(none_stop=True)