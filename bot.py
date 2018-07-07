import telebot
from telebot import types

TOKEN = '587528180:AAG4hsUKfoguxfkSEeyTzrD65PMKuy3EPbU'

bot = telebot.TeleBot(TOKEN)

greeting = 'Это бот блаблабла\n коротко о командах: бла бла бла'

@bot.message_handler(commands=['start'])
def start(m):

	#toDo: связать с командой Меню кнопку Меню


    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('меню'))

    msg=bot.send_message(m.chat.id, greeting,
        reply_markup=keyboard)
    # bot.register_next_step_handler(msg, name)


@bot.message_handler(commands=['menu'])
def menu(m):
    
    #toDO: написать функцию, которая в зависимости от выбр кнопки вызывает команду. 

	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Калькулятор',
        'Помощь']])
    keyboard.add(types.KeyboardButton('Сайт'))     #сайт кнопка-ссылка



@bot.message_handler(commands=['help'])
def help(m):

	#Todo: обеспечить выходв меню, кнопку там после хелпы чтоль дать

	detailedCommandsInfo = ' /calc is bla bla /site is bla bla bla'

	bot.send_message(message.chat.id, detailedCommandsInfo)


@bot.message_handler(commands=['calc'])								#калькулятор можно в отдельный класс и все функции там прописать
def calc(m):

	msg=bot.send_message(m.chat.id, greeting,
        reply_markup=keyboard)
    # bot.register_next_step_handler(msg, name)


bot.polling(none_stop=True)