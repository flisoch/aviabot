import datetime

import telebot
from telebot import types
from aviabot.telegramcalendar import create_calendar

current_shown_dates = {}


def fetch_cities(cities_as_string):
    return None


def step2_get_calendar(message, bot):
    now = datetime.datetime.now()  # Current date
    chat_id = message.chat.id
    date = (now.year, now.month)
    current_shown_dates[chat_id] = date  # Saving the current date in a dict
    markup = create_calendar(now.year, now.month, chosen_day=now.day)
    bot.send_message(message.chat.id, "Please, choose a date", reply_markup=markup)


def step1(msg, bot):
    cities = bot.get_updates(msg.chat.id)[-1]
    cities_information = fetch_cities(cities)  # вытащить с базе данных всё с этими городами

    if cities_information is not None or cities.message.text == "Ташкент Москва":  # заглушка с городами
        step2_get_calendar(msg, bot)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(types.KeyboardButton(text="Калькулятор"))
        keyboard.add(types.KeyboardButton(text="Меню"))

        bot.send_message(msg.chat.id,
                         text="К сожалению, билетов по таким направлениям нет\n"
                              "Вы можете выбрать другие города или выйти в главное меню",
                         reply_markup=keyboard)


def calculate(msg, bot):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(msg.chat.id, "введите uchish shahari va qo'nish shahari через пробел, like this:\n"
                                  "Ташкент Москва", reply_markup=markup)
