import requests, telebot
from telebot import types
TOKEN = "1020454335:AAF1Xoi70lyUdj8gunEvh6G1GOanOzLRv3E"
bot = telebot.TeleBot(TOKEN)

kb1 = types.InlineKeyboardMarkup(row_width=1)
b1 = types.InlineKeyboardButton(text="Выбрать город", callback_data="b1")
kb1.add(b1)

kb2 = types.InlineKeyboardMarkup(row_width=1)
alf1 = types.InlineKeyboardButton(text="А Б В Г", callback_data="alf1")
alf2 = types.InlineKeyboardButton(text="Д Е Ж З", callback_data="alf2")
alf3 = types.InlineKeyboardButton(text="И К Л", callback_data="alf3")
alf4 = types.InlineKeyboardButton(text="М Н О П", callback_data="alf4")
alf5 = types.InlineKeyboardButton(text="Р С Т У", callback_data="alf5")
alf6 = types.InlineKeyboardButton(text="Ф Х Ц Ш Щ", callback_data="alf6")
alf7 = types.InlineKeyboardButton(text="Э Ю Я", callback_data="alf7")
kb2.add(alf1, alf2, alf3, alf4, alf5, alf6, alf7)

city1 = types.InlineKeyboardMarkup(row_width=1)
c11 = types.InlineKeyboardButton(text="Архангельск", callback_data="choice")
c12 = types.InlineKeyboardButton(text="Анапа", callback_data="choice")
c13 = types.InlineKeyboardButton(text="Астрахань", callback_data="choice")
c14 = types.InlineKeyboardButton(text="Барнаул", callback_data="choice")
c15 = types.InlineKeyboardButton(text="Белгород", callback_data="choice")
c16 = types.InlineKeyboardButton(text="Брянск", callback_data="choice")
c17 = types.InlineKeyboardButton(text="Великий Новгород", callback_data="choice")
c18 = types.InlineKeyboardButton(text="Владикавказ", callback_data="choice")
c19 = types.InlineKeyboardButton(text="Владимир", callback_data="choice")
c110 = types.InlineKeyboardButton(text="Воронеж", callback_data="choice")
c111 = types.InlineKeyboardButton(text="Геленджик", callback_data="choice")
city1.add(c11, c12, c13, c14, c15, c16, c17, c18, c19, c110, c111)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, text='Здравствуйте! Вас приветствует бот автопродаж PureMagic! Для начала давайте определимся с городом', reply_markup=kb1)

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == 'b1':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Выберите первую букву Вашего города", reply_markup=kb2)
    if c.data == 'alf1':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Выберите Ваш город", reply_markup=city1)

#@bot.message_handler(content_types=['text'])
#def text_handler(message):
#    text = message.text.lower()
#    chat_id = message.chat.id
#    if text == "привет":
#        bot.send_message(chat_id, 'Привет, я бот - парсер хабра.')
#    elif text == "как дела?":
#        bot.send_message(chat_id, 'Хорошо, а у тебя?')
#    else:
#        bot.send_message(chat_id, 'Простите, я вас не понял :(')
        
if __name__ == '__main__':
     bot.polling(none_stop=True)

