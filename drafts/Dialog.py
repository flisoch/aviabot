import telebot

TOKEN = '498239431:AAGTeky5z-giYCC7VazGPScgF9hXFTqrbZw'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Соски сосёшь?')
    bot.register_next_step_handler(sent, hello)
def hello(message):
    bot.send_message(
    message.chat.id,
    '{name}? Не ожидал!'.format(name=message.text))

bot.polling(none_stop=True)