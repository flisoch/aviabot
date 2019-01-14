# -*- encoding: utf-8 -*-
import datetime
import time

import telebot
from telebot import types
import secret
from Calculator import *

bot = telebot.TeleBot(secret.TOKEN, threaded=False)


@bot.message_handler(commands=['start'])
def start(msg):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Меню"))
    greeting = 'Этот бот поможет вам узнать цены на рейсы по выбранным вами направлениям перелёта\n' \
               'Доступные команды:\n/calc - подсчитает стоимость перелёта\n' \
               '/help - помощь по командам бота\n' \
               '/menu - меню бота'

    bot.send_message(msg.chat.id, greeting, reply_markup=keyboard)


@bot.message_handler(func=lambda message:message.text in ['Назад к выбору города','Калькулятор',
                                                          'К выбору городов',"Изменить города"])
def extra_calc(msg):
    calc(msg)


@bot.message_handler(regex="Изменить дату вылета")
def change_vilet_date(message):
    print("menyaem")
    step2_show_calendar(message)

@bot.message_handler(commands=['calc'])
def calc(m):
    calculate(m)


@bot.message_handler(regexp='Наш Сайт')
def site(msg):
    date = str(datetime.datetime.now()).split()[0]
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Перейти на сайт',
                                            url='https://www.uzairways.com/ru/tariffcalc?currency=UZS&'
                                                'tablofrom=TAS&tabloto=IST&'
                                                'date=' + date))
    bot.send_message(msg.chat.id, "Чтобы перейти на наш сайт, нажмите кнопку ниже", reply_markup=markup)


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
    print(msg.chat)
    # bot.register_next_step_handler(message=msg, callback=menu_func(msg))


@bot.message_handler(regexp='(М|м)еню')
def extra_menu(msg):
    menu(msg)


@bot.message_handler(commands=['help'])
def help(message):
    detailedCommandsInfo = ' Доступные команды бота:\n\n' \
                           '/calc введите то сё(описание всех шагов)\n\n' \
                           '/menu вызовет меню бота, откуда можно работать без вызова команд\n\n' \
                           '/help - помощь по использованию бота\n\n' \
                           'На наш сайт можно выйти из Меню\n\n'
    bot.send_message(message.chat.id, detailedCommandsInfo)


@bot.message_handler(regexp='Помощь')
def extra_help(message):
    help(message)


@bot.message_handler(regexp="[a-zA-Zа-яА-Я0-9]\s+[a-zA-Zа-яА-Я0-9]")
def step11(m):
    step1(m)


@bot.callback_query_handler(func=lambda call: "second-calendar-day" in call.data)
def get_day_second_call(call):
    calendar_hadnler(call,is_second_call=True)


@bot.callback_query_handler(func=lambda call: "first-calendar-day" in call.data)  # к бд за датой,есть ли вообще
def get_day(call):
    calendar_hadnler(call)


@bot.callback_query_handler(func=lambda call: call.data == 'next-month')
def next_month(call):
    print(current_shown_dates)
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    if (saved_date is not None):
        year, month = saved_date
        month += 1
        if month > 12:
            month = 1
            year += 1
        date = (year, month)
        current_shown_dates[chat_id] = date

        markup = create_calendar(year, month, chosen_day=0)
        bot.edit_message_text("Please, choose a date", call.from_user.id, call.message.message_id, reply_markup=markup)
        bot.answer_callback_query(call.id, text="")
    else:
        # Do something to inform of the error
        pass


@bot.callback_query_handler(func=lambda call: call.data == 'previous-month')
def previous_month(call):
    print(current_shown_dates)
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    if (saved_date is not None):
        year, month = saved_date
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        date = (year, month)
        current_shown_dates[chat_id] = date
        markup = create_calendar(year, month, chosen_day=0)
        bot.edit_message_text("Please, choose a date", call.from_user.id, call.message.message_id, reply_markup=markup)
        bot.answer_callback_query(call.id, text="")
    else:
        # Do something to inform of the error
        pass


@bot.callback_query_handler(func=lambda call: call.data == 'ignore')
def ignore(call):
    bot.answer_callback_query(call.id, text="")


while True:
    try:
        bot.polling(none_stop=True, timeout=31)
    except Exception as e:
        telebot.logger.error(e)
        time.sleep(15)
