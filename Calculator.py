import datetime
import time

import telebot
from telebot import types

import secret
from telegramcalendar import create_calendar

current_shown_dates = {}

bot = telebot.TeleBot(secret.TOKEN, threaded=False)

def fetch_info(cities_as_string):
    return None


def step2_show_calendar(message):
    print(message)
    now = datetime.datetime.now()  # Current date
    chat_id = message.chat.id
    date = (now.year, now.month)
    current_shown_dates[chat_id] = date  # Saving the current date in a dict
    markup = create_calendar(now.year, now.month, chosen_day=now.day)
    bot.send_message(message.chat.id, "Пожалуйста,выберете дату вылета", reply_markup=markup)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Назад к выбору города"))
    msg = bot.send_message(message.chat.id,"Вы можете изменить город",reply_markup=markup)


def last_message_from_user(chat_id):
    return bot.get_updates(chat_id)[-1]


def step1(msg):
    #Todo: подкл к бд за инфой о запрашиваемых городах

    cities = last_message_from_user(msg.chat.id)
    cities_information = fetch_info(cities)  # вытащить с базе данных всё с этими городами

    if cities_information is not None or cities.message.text == "Ташкент Москва":  # заглушка с городами
        step2_show_calendar(msg)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(types.KeyboardButton(text="К выбору городов"))
        keyboard.add(types.KeyboardButton(text="Меню"))

        bot.send_message(msg.chat.id,
                         text="К сожалению, билетов по таким направлениям нет\n"
                              "Вы можете выбрать другие города или выйти в главное меню",
                         reply_markup=keyboard)


def calculate(msg):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(msg.chat.id, "введите uchish shahari va qo'nish shahari через пробел, like this:\n"
                                  "Ташкент Москва", reply_markup=markup)


def calc_sum():  # к бд за стоимостью
    return "575 999"


def total_info():
    return 'Стоимость перелёта:' + calc_sum()


def calendar_hadnler(call,is_second_call=False):
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    if (saved_date is not None):
        data = call.data.split()
        day = data[1]
        month = data[2]
        year = data[3]
        date = datetime.datetime(int(saved_date[0]), int(saved_date[1]), int(day), 0, 0, 0)

        if is_second_call:

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
            markup.add(types.KeyboardButton("Меню"))
            bot.send_message(chat_id, 'Дата прилёта: ' + str(date), reply_markup=markup)
            bot.send_message(chat_id, total_info())

        else:
            # bot.edit_message_text(text=str(date),chat_id=chat_id,message_id=call.message.message_id+1)
            bot.delete_message(chat_id,call.message.message_id+1)

            markup = create_calendar(int(year), int(month), chosen_day=int(day), is_second_call=True)
            bot.edit_message_reply_markup(chat_id,message_id=call.message.message_id,reply_markup=markup)

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton("Изменить дату вылета"))
            markup.add(types.KeyboardButton("Изменить города"))
            bot.send_message(chat_id, 'Теперь выберите дату прилёта',reply_markup=markup)



    else:
        # Do something to inform of the error
        print("data is None")
        bot.answer_callback_query(call.id, text="data is None")
        pass