import telebot
TOKEN = '498239431:AAGTeky5z-giYCC7VazGPScgF9hXFTqrbZw'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def request_contact(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_contact = types.KeyboardButton(text="START", request_contact=True)
    keyboard.add(button_contact)
    msg = bot.send_message(message.chat.id, "Ув.пользовател, для начало работы с ботом нажмите на кнопку 'START' 😊 ", reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)

def start(message):
    #Переводы
    if cons.lang == 'ru':
      start_msg = 'Здравствуйте, уважаемый клиент!\nВас приветствует бот компании!\nПожалуйста, выберите из меню то что вас интересует.'
      order_menu = 'Заказать такси'
      info_menu = 'Информация'
      exit_menu = 'Покинуть бота'
    elif cons.lang == 'en':
      start_msg = 'Grettings.'
      order_menu = 'Order Taxi'
      info_menu = 'Information'
      exit_menu = 'Leave bot'

  # Главное меню
    start_markup = types.ReplyKeyboardMarkup(True, False)
    start_markup.row('🚕 '+cons.order_menu+' 🚕', )
    start_markup.row('ℹ️ '+cons.info_menu+' ℹ️')
    start_markup.row('English', 'Русский язык')
    start_markup.row('🚪 '+cons.exit_menu+' 🚪')
    bot.send_message(message.chat.id, cons.start_msg, reply_markup=start_markup)

@bot.message_handler(content_types=["text"])
def main(message): 
    if message.text == 'English':
        cons.lang = 'en'
        msg = bot.send_message(message.chat.id, 'Your language is -'+cons.lang+' -', reply_markup=start_markup)
        bot.register_next_step_handler(msg, start)
    elif message.text == 'Русский язык':
        cons.lang = 'ru'
        msg = bot.send_message(message.chat.id, 'Вы выбрали русский язык-'+cons.lang+' -', reply_markup=start_markup)
        bot.register_next_step_handler(msg, start)

bot.polling(none_stop=True)