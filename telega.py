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

city2 = types.InlineKeyboardMarkup(row_width=1)
c21 = types.InlineKeyboardButton(text="Дзержинск", callback_data="choice")
c22 = types.InlineKeyboardButton(text="Долгопрудный", callback_data="choice")
c23 = types.InlineKeyboardButton(text="Екатеринбург", callback_data="choice")
c24 = types.InlineKeyboardButton(text="Жуковский", callback_data="choice")
c25 = types.InlineKeyboardButton(text="Зеленогорск", callback_data="choice")
city2.add(c21, c22, c23, c24, c25)

city3 = types.InlineKeyboardMarkup(row_width=1)
c31 = types.InlineKeyboardButton(text="Ижевск", callback_data="choice")
c32 = types.InlineKeyboardButton(text="Иркутск", callback_data="choice")
c33 = types.InlineKeyboardButton(text="Казань", callback_data="choice")
c34 = types.InlineKeyboardButton(text="Калининград", callback_data="choice")
c35 = types.InlineKeyboardButton(text="Калуга", callback_data="choice")
c36 = types.InlineKeyboardButton(text="Керчь", callback_data="choice")
c37 = types.InlineKeyboardButton(text="Киров", callback_data="choice")
c38 = types.InlineKeyboardButton(text="Коломна", callback_data="choice")
c39 = types.InlineKeyboardButton(text="Кострома", callback_data="choice")
c310 = types.InlineKeyboardButton(text="Краснодар", callback_data="choice")
c311 = types.InlineKeyboardButton(text="Липецк", callback_data="choice")
c312 = types.InlineKeyboardButton(text="Люберцы", callback_data="choice")
city3.add(c31, c32, c33, c34, c35, c36, c37, c38, c39, c310, c311, c312)

city4 = types.InlineKeyboardMarkup(row_width=1)
c41 = types.InlineKeyboardButton(text="Москва", callback_data="choice")
c42 = types.InlineKeyboardButton(text="Мурманск", callback_data="choice")
c43 = types.InlineKeyboardButton(text="Мытищи", callback_data="choice")
c44 = types.InlineKeyboardButton(text="Махачкала", callback_data="choice")
c45 = types.InlineKeyboardButton(text="Нальчик", callback_data="choice")
c46 = types.InlineKeyboardButton(text="Нижний Новгород", callback_data="choice")
c47 = types.InlineKeyboardButton(text="Новокузнецк", callback_data="choice")
c48 = types.InlineKeyboardButton(text="Одинцово", callback_data="choice")
c49 = types.InlineKeyboardButton(text="Омск", callback_data="choice")
c410 = types.InlineKeyboardButton(text="Оренбург", callback_data="choice")
c411 = types.InlineKeyboardButton(text="Пермь", callback_data="choice")
c412 = types.InlineKeyboardButton(text="Петрозаводск", callback_data="choice")
c413 = types.InlineKeyboardButton(text="Псков", callback_data="choice")
city4.add(c41, c42, c43, c44, c45, c46, c47, c48, c49, c410, c411, c412, c413)

city5 = types.InlineKeyboardMarkup(row_width=1)
c51 = types.InlineKeyboardButton(text="Раменское", callback_data="choice")
c52 = types.InlineKeyboardButton(text="Ростов-на-Дону", callback_data="choice")
c53 = types.InlineKeyboardButton(text="Рязань", callback_data="choice")
c54 = types.InlineKeyboardButton(text="Самара", callback_data="choice")
c55 = types.InlineKeyboardButton(text="Санкт-Петербург", callback_data="choice")
c56 = types.InlineKeyboardButton(text="Саратов", callback_data="choice")
c57 = types.InlineKeyboardButton(text="Севастополь", callback_data="choice")
c58 = types.InlineKeyboardButton(text="Серпухов", callback_data="choice")
c59 = types.InlineKeyboardButton(text="Сочи", callback_data="choice")
c510 = types.InlineKeyboardButton(text="Ставрополь", callback_data="choice")
c511 = types.InlineKeyboardButton(text="Тамбов", callback_data="choice")
c512 = types.InlineKeyboardButton(text="Тверь", callback_data="choice")
c513 = types.InlineKeyboardButton(text="Томск", callback_data="choice")
c514 = types.InlineKeyboardButton(text="Тюмень", callback_data="choice")
c515 = types.InlineKeyboardButton(text="Улан-Удэ", callback_data="choice")
c516 = types.InlineKeyboardButton(text="Уфа", callback_data="choice")
city5.add(c51, c52, c53, c54, c55, c56, c57, c58, c59, c510, c511, c512, c513, c514, c515, c516)

city6 = types.InlineKeyboardMarkup(row_width=1)
c61 = types.InlineKeyboardButton(text="Хабаровск", callback_data="choice")
c62 = types.InlineKeyboardButton(text="Ханты-Мансийск", callback_data="choice")
c63 = types.InlineKeyboardButton(text="Химки", callback_data="choice")
c64 = types.InlineKeyboardButton(text="Челябинск", callback_data="choice")
c65 = types.InlineKeyboardButton(text="Чехов", callback_data="choice")
c66 = types.InlineKeyboardButton(text="Чита", callback_data="choice")
c67 = types.InlineKeyboardButton(text="Щелково", callback_data="choice")
city6.add(c61, c62, c63, c64, c65, c66, c67)

city7 = types.InlineKeyboardMarkup(row_width=1)
c71 = types.InlineKeyboardButton(text="Электросталь", callback_data="choice")
c72 = types.InlineKeyboardButton(text="Южно-Сахалинск", callback_data="choice")
c73 = types.InlineKeyboardButton(text="Якутск", callback_data="choice")
c74 = types.InlineKeyboardButton(text="Ялта", callback_data="choice")
c75 = types.InlineKeyboardButton(text="Ярославль", callback_data="choice")
city7.add(c71, c72, c73, c74, c75)

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

