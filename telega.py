import requests, telebot, random
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
back = types.InlineKeyboardButton(text="<< Назад", callback_data="back")
kb2.add(alf1, alf2, alf3, alf4, alf5, alf6, alf7)

kb3 = types.InlineKeyboardMarkup(row_width=1)
t1 = types.InlineKeyboardButton(text="Марихуана 1г", callback_data="mj1")
t2 = types.InlineKeyboardButton(text="Марихуана 3г", callback_data="mj3")
t3 = types.InlineKeyboardButton(text="Гашиш 2г", callback_data="g2")
t4 = types.InlineKeyboardButton(text="Мефедрон 1г", callback_data="m1")
t5 = types.InlineKeyboardButton(text="Мефедрон 2г", callback_data="m2")
t6 = types.InlineKeyboardButton(text="Мефедрон 5г", callback_data="m5")
t7 = types.InlineKeyboardButton(text="ЛСД 2 по 250мг", callback_data="l250")
kb3.add(t1, t2, t3, t4, t5, t6, t7)

city1 = types.InlineKeyboardMarkup(row_width=1)
c11 = types.InlineKeyboardButton(text="Архангельcк", callback_data="choice")
c12 = types.InlineKeyboardButton(text="Анапа", callback_data="choice")
c13 = types.InlineKeyboardButton(text="Аcтрахань", callback_data="choice")
c14 = types.InlineKeyboardButton(text="Барнаул", callback_data="choice")
c15 = types.InlineKeyboardButton(text="Белгород", callback_data="choice")
c16 = types.InlineKeyboardButton(text="Брянcк", callback_data="choice")
c17 = types.InlineKeyboardButton(text="Великий Новгород", callback_data="choice")
c18 = types.InlineKeyboardButton(text="Владикавказ", callback_data="choice")
c19 = types.InlineKeyboardButton(text="Владимир", callback_data="choice")
c110 = types.InlineKeyboardButton(text="Воронеж", callback_data="choice")
c111 = types.InlineKeyboardButton(text="Геленджик", callback_data="choice")
city1.add(c11, c12, c13, c14, c15, c16, c17, c18, c19, c110, c111, back)

city2 = types.InlineKeyboardMarkup(row_width=1)
c21 = types.InlineKeyboardButton(text="Дзержинcк", callback_data="choice")
c22 = types.InlineKeyboardButton(text="Долгопрудный", callback_data="choice")
c23 = types.InlineKeyboardButton(text="Екатеринбург", callback_data="choice")
c24 = types.InlineKeyboardButton(text="Жуковcкий", callback_data="choice")
c25 = types.InlineKeyboardButton(text="Зеленогорcк", callback_data="choice")
city2.add(c21, c22, c23, c24, c25, back)

city3 = types.InlineKeyboardMarkup(row_width=1)
c31 = types.InlineKeyboardButton(text="Ижевcк", callback_data="choice")
c32 = types.InlineKeyboardButton(text="Иркутcк", callback_data="choice")
c33 = types.InlineKeyboardButton(text="Казань", callback_data="choice")
c34 = types.InlineKeyboardButton(text="Калининград", callback_data="choice")
c35 = types.InlineKeyboardButton(text="Калуга", callback_data="choice")
c36 = types.InlineKeyboardButton(text="Керчь", callback_data="choice")
c37 = types.InlineKeyboardButton(text="Киров", callback_data="choice")
c38 = types.InlineKeyboardButton(text="Коломна", callback_data="choice")
c39 = types.InlineKeyboardButton(text="Коcтрома", callback_data="choice")
c310 = types.InlineKeyboardButton(text="Краcнодар", callback_data="choice")
c311 = types.InlineKeyboardButton(text="Липецк", callback_data="choice")
c312 = types.InlineKeyboardButton(text="Люберцы", callback_data="choice")
city3.add(c31, c32, c33, c34, c35, c36, c37, c38, c39, c310, c311, c312, back)

city4 = types.InlineKeyboardMarkup(row_width=1)
c41 = types.InlineKeyboardButton(text="Моcква", callback_data="choice")
c42 = types.InlineKeyboardButton(text="Мурманcк", callback_data="choice")
c43 = types.InlineKeyboardButton(text="Мытищи", callback_data="choice")
c44 = types.InlineKeyboardButton(text="Махачкала", callback_data="choice")
c45 = types.InlineKeyboardButton(text="Нальчик", callback_data="choice")
c46 = types.InlineKeyboardButton(text="Нижний Новгород", callback_data="choice")
c47 = types.InlineKeyboardButton(text="Новокузнецк", callback_data="choice")
c48 = types.InlineKeyboardButton(text="Одинцово", callback_data="choice")
c49 = types.InlineKeyboardButton(text="Омcк", callback_data="choice")
c410 = types.InlineKeyboardButton(text="Оренбург", callback_data="choice")
c411 = types.InlineKeyboardButton(text="Пермь", callback_data="choice")
c412 = types.InlineKeyboardButton(text="Петрозаводcк", callback_data="choice")
c413 = types.InlineKeyboardButton(text="Пcков", callback_data="choice")
city4.add(c41, c42, c43, c44, c45, c46, c47, c48, c49, c410, c411, c412, c413, back)

city5 = types.InlineKeyboardMarkup(row_width=1)
c51 = types.InlineKeyboardButton(text="Раменcкое", callback_data="choice")
c52 = types.InlineKeyboardButton(text="Роcтов-на-Дону", callback_data="choice")
c53 = types.InlineKeyboardButton(text="Рязань", callback_data="choice")
c54 = types.InlineKeyboardButton(text="Самара", callback_data="choice")
c55 = types.InlineKeyboardButton(text="Санкт-Петербург", callback_data="choice")
c56 = types.InlineKeyboardButton(text="Саратов", callback_data="choice")
c57 = types.InlineKeyboardButton(text="Севаcтополь", callback_data="choice")
c58 = types.InlineKeyboardButton(text="Серпухов", callback_data="choice")
c59 = types.InlineKeyboardButton(text="Сочи", callback_data="choice")
c510 = types.InlineKeyboardButton(text="Ставрополь", callback_data="choice")
c511 = types.InlineKeyboardButton(text="Тамбов", callback_data="choice")
c512 = types.InlineKeyboardButton(text="Тверь", callback_data="choice")
c513 = types.InlineKeyboardButton(text="Томcк", callback_data="choice")
c514 = types.InlineKeyboardButton(text="Тюмень", callback_data="choice")
c515 = types.InlineKeyboardButton(text="Улан-Удэ", callback_data="choice")
c516 = types.InlineKeyboardButton(text="Уфа", callback_data="choice")
city5.add(c51, c52, c53, c54, c55, c56, c57, c58, c59, c510, c511, c512, c513, c514, c515, c516, back)

city6 = types.InlineKeyboardMarkup(row_width=1)
c61 = types.InlineKeyboardButton(text="Хабаровcк", callback_data="choice")
c62 = types.InlineKeyboardButton(text="Ханты-Манcийcк", callback_data="choice")
c63 = types.InlineKeyboardButton(text="Химки", callback_data="choice")
c64 = types.InlineKeyboardButton(text="Челябинcк", callback_data="choice")
c65 = types.InlineKeyboardButton(text="Чехов", callback_data="choice")
c66 = types.InlineKeyboardButton(text="Чита", callback_data="choice")
c67 = types.InlineKeyboardButton(text="Щелково", callback_data="choice")
city6.add(c61, c62, c63, c64, c65, c66, c67, back)

city7 = types.InlineKeyboardMarkup(row_width=1)
c71 = types.InlineKeyboardButton(text="Электроcталь", callback_data="choice")
c72 = types.InlineKeyboardButton(text="Южно-cахалинcк", callback_data="choice")
c73 = types.InlineKeyboardButton(text="Якутcк", callback_data="choice")
c74 = types.InlineKeyboardButton(text="Ялта", callback_data="choice")
c75 = types.InlineKeyboardButton(text="Яроcлавль", callback_data="choice")
city7.add(c71, c72, c73, c74, c75, back)

check = types.InlineKeyboardMarkup(row_width=1)
check1 = types.InlineKeyboardButton(text="Проверить оплату", callback_data="fuckoff")
check.add(check1)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, text='Здравcтвуйте! Ваc приветcтвует бот автопродаж PureMagic! Для начала давайте определимcя c городом', reply_markup=kb1)

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == 'b1':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Выберите первую букву Вашего города", reply_markup=kb2)
    if c.data == 'alf1':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Выберите Ваш город", reply_markup=city1)
    if c.data == 'alf2':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Выберите Ваш город", reply_markup=city2)
    if c.data == 'alf3':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Выберите Ваш город", reply_markup=city3)
    if c.data == 'alf4':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Выберите Ваш город", reply_markup=city4)
    if c.data == 'alf5':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Выберите Ваш город", reply_markup=city5)
    if c.data == 'alf6':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Выберите Ваш город", reply_markup=city6)
    if c.data == 'alf7':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Выберите Ваш город", reply_markup=city7)
    if c.data == 'back':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Выберите первую букву Вашего города", reply_markup=kb2)
    if c.data == 'choice':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Выберите товар", reply_markup=kb3)
    if c.data == 'mj1':
        number = str(random.randint(100000,999999))
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Вы выбрали: Марихуана 1г \nЦена: 1200₽ \nОплата принимается на Яндекс Деньги: 43575638 \nили на Qiwi: 865394865937456 \nКод в комментарии: " + number + "\nПосле оплаты нажмите на кнопку 'Проверить оплату'. Транзакции проверяются вручную. Примерное время подтверждения составляет 15 минут. После того, как оператор удостоверится в успешности оплаты, Вам придет фото, координаты и описание места", reply_markup=check)
    if c.data == 'mj3':
        number = str(random.randint(100000,999999))
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Вы выбрали: Марихуана 3г \nЦена: 2500₽ \nОплата принимается на Яндекс Деньги: 43575638 \nили на Qiwi: 865394865937456 \nКод в комментарии: " + number + "\nПосле оплаты нажмите на кнопку 'Проверить оплату'. Транзакции проверяются вручную. Примерное время подтверждения составляет 15 минут. После того, как оператор удостоверится в успешности оплаты, Вам придет фото, координаты и описание места", reply_markup=check)
    if c.data == 'g2':
        number = str(random.randint(100000,999999))
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Вы выбрали: Гашиш 2г \nЦена: 1400₽ \nОплата принимается на Яндекс Деньги: 43575638 \nили на Qiwi: 865394865937456 \nКод в комментарии: " + number + "\nПосле оплаты нажмите на кнопку 'Проверить оплату'. Транзакции проверяются вручную. Примерное время подтверждения составляет 15 минут. После того, как оператор удостоверится в успешности оплаты, Вам придет фото, координаты и описание места", reply_markup=check)
    if c.data == 'm1':
        number = str(random.randint(100000,999999))
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Вы выбрали: Мефедрон 1г \nЦена: 1100₽ \nОплата принимается на Яндекс Деньги: 43575638 \nили на Qiwi: 865394865937456 \nКод в комментарии: " + number + "\nПосле оплаты нажмите на кнопку 'Проверить оплату'. Транзакции проверяются вручную. Примерное время подтверждения составляет 15 минут. После того, как оператор удостоверится в успешности оплаты, Вам придет фото, координаты и описание места", reply_markup=check)
    if c.data == 'm2':
        number = str(random.randint(100000,999999))
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Вы выбрали: Мефедрон 2г \nЦена: 2000₽ \nОплата принимается на Яндекс Деньги: 43575638 \nили на Qiwi: 865394865937456 \nКод в комментарии: " + number + "\nПосле оплаты нажмите на кнопку 'Проверить оплату'. Транзакции проверяются вручную. Примерное время подтверждения составляет 15 минут. После того, как оператор удостоверится в успешности оплаты, Вам придет фото, координаты и описание места", reply_markup=check)
    if c.data == 'm5':
        number = str(random.randint(100000,999999))
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Вы выбрали: Мефедрон 5г \nЦена: 3500₽ \nОплата принимается на Яндекс Деньги: 43575638 \nили на Qiwi: 865394865937456 \nКод в комментарии: " + number + "\nПосле оплаты нажмите на кнопку 'Проверить оплату'. Транзакции проверяются вручную. Примерное время подтверждения составляет 15 минут. После того, как оператор удостоверится в успешности оплаты, Вам придет фото, координаты и описание места", reply_markup=check)
    if c.data == 'l250':
        number = str(random.randint(100000,999999))
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Вы выбрали: ЛСД 2 по 250мг \nЦена: 2900₽ \nОплата принимается на Яндекс Деньги: 43575638 \nили на Qiwi: 865394865937456 \nКод в комментарии: " + number + "\nПосле оплаты нажмите на кнопку 'Проверить оплату'. Транзакции проверяются вручную. Примерное время подтверждения составляет 15 минут. После того, как оператор удостоверится в успешности оплаты, Вам придет фото, координаты и описание места", reply_markup=check)

        
if __name__ == '__main__':
     bot.polling(none_stop=True)


