import telebot
from telebot import types

TOKEN = '498239431:AAGTeky5z-giYCC7VazGPScgF9hXFTqrbZw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Мирабад',
        'Хамза', 'Учтепа']])
    msg=bot.send_message(m.chat.id, 'В каком районе вы находитесь?',
        reply_markup=keyboard)
    bot. register_next_step_handler(msg, name)

def name(m):
    if m.text=='Мирабад':
        bot.send_message(m.chat.id, '*Шерлок Холмс*-детектив-консултант.',
            parse_mode='Markdown')
    elif m.text=='Хамза':
        bot.send_message(m.chat.id, '*Доктор Ватсон*-лучший друг Шерлока.',
            parse_mode='Markdown')

bot.polling(none_stop=True)