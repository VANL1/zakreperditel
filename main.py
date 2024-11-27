import telebot
import bs_api
import config
from random import randint
from time import sleep

bot = telebot.TeleBot(config.token_tg)


@bot.message_handler(commands=['start', 'pp', 'sigma', 'trophies', 'victories', 'total_sigma'])
def start(message):
    if '/start' in message.text:
        bot.send_message(message.chat.id, "Пук пуги кагажки пертеж пипэски")
    elif '/pp' in message.text:
        x = randint(0, 8)
        bot.reply_to(message, config.penises[int(x)])
    elif '/sigma' in message.text:
        bot.send_photo(message.chat.id, photo=open('photo.png', 'rb'))
    elif '/trophies' in message.text:
        bot.send_message(message.chat.id,
                         f'Сигма игрок в бравл старс {bs_api.nickname()} сейчас имеет \033{bs_api.trophies()}\033 кубков')
    elif '/victories' in message.text:
        bot.send_message(message.chat.id, f'Сигма игрок в бравл старс {bs_api.nickname()} сейчас имеет:\n'
                                          f'{bs_api.victories()[0]} побед в соло шд\n'
                                          f'{bs_api.victories()[1]} побед в дуо шд\n'
                                          f'{bs_api.victories()[2]} побед в 3 на 3')
    elif '/total_sigma' in message.text:
        bot.send_message(message.chat.id,
                         f'{bs_api.nickname()} НСТОЛЬКО СИГМА, ЧТО У НЕГО {bs_api.trophies()} КУБУОВ {bs_api.victories()[0]} ПОБЕД В СОЛО ШД,'
                         f'{bs_api.victories()[1]} ПОБЕД В ДУО ШД И '
                         f'{bs_api.victories()[2]} ПОБЕД B 3 НА 3, А СУММАРНО У НЕГО {bs_api.sum_victories()} ПОБЕД')
        bot.send_message(message.chat.id, 'ЕБАТЬ ОН СИГМА')


@bot.message_handler(content_types=['text'])
def what(message):
    if message.text == 'Что?':
        sleep(2)
        bot.reply_to(message, "Паташти, йа ни такафарил")
        sleep(3)
        bot.send_message(message.chat.id, 'ЖОПА ПАНОС КАВНО')


@bot.message_handler(content_types=['poll'])
def f(message):
    bot.pin_chat_message(message.chat.id, message.id)


bot.polling(none_stop=True)
