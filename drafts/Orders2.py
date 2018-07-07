import telebot
from telebot import types

TOKEN = '498239431:AAGTeky5z-giYCC7VazGPScgF9hXFTqrbZw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Сделать заказ!']])
    msg=bot.send_message(m.chat.id, '*Сделать заказ стало еще проще!*\n1.Мы сэкономим Ваше время.\n2.Мы сэкономим Ваши деньги.\n3.Мы сделаем все проще и быстрее для Вас!',
        reply_markup=keyboard)
    bot. register_next_step_handler(msg, district)
def district(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Мирабад',
        'Хамзинский', 'Учтепа','Чиланзар','Юнусабад','Мирзо Улугбек',
        'Сергели','Бектимир','Яккасарай','Олмазар','Шайхантахур']])
    msg=bot.send_message(m.chat.id, 'Выберите район, в котором вы находитесь?',
        reply_markup=keyboard)
    bot. register_next_step_handler(msg, summa)
def summa(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Около 100 000',
        'Около 500 000', 'Около 1 000 000', 'Не знаю', 'Акции!']])
    msg=bot.send_message(m.chat.id, 'Пожалуйста, выберите приблизительную сумму заказа?',
        reply_markup=keyboard)
    bot. register_next_step_handler(msg, information)
def information(m):
    markup = types.ForceReply ( selective = False )
    msg=bot.send_message(m.chat.id, 'Пожалуйста, введите Ваш номер телефона, имя(через пробел) и отправьте как обычное сообщение.',
        reply_markup=markup)
    bot. register_next_step_handler(msg, start)

bot.polling(none_stop=True)