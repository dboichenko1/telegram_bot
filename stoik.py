import time
import telebot
import schedule
import json
import random
import math
import os 
token = "" #доделать переменные окружения
my_chat_id = ""
bot = telebot.TeleBot(token)

def to_roman(num):
    '''
    перевод чисел в римскую систему счисления
    принимает инт число,
    возвращает римское число строку
    '''
    all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman = ''
    while num > 0:
        for i, r in all_roman:
            while num >= i:
                roman += r
                num -= i
    return roman

def send_message():
    '''
    Отправка сообщения
    '''
    random_letter = random.randint(0,124)
    with open ("pisma.json", "r") as q:
        pisma_dict = json.load(q)
    message = f"Письмо {to_roman(random_letter)}\n{pisma_dict[f'Письмо {to_roman(random_letter)}']}"
    #если размер сообщения выходит за лимит телеги, отправляем разными сообщениями ceil - округляет в большую сторону
    if len(message) > 4095:
        telegram_message_limit = 4095
        qty_block = math.ceil(len(message)/telegram_message_limit)
        for i in range(qty_block):
            bot.send_message(chat_id=my_chat_id, text=message[i*telegram_message_limit:(i+1)*telegram_message_limit])
    else:
        bot.send_message(chat_id=my_chat_id, text=message)




# Планировщик отправки сообщения
schedule.every().day.at("08:00").do(send_message)
# schedule.every().minute.at(":01").do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)