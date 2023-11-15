from telebot import types, telebot

bot = telebot.TeleBot("          ")

db = {'ФИО': 'Карпушев Алексей', 'Адрес': 'ул. Ленина', 'Работа': 'ИФ'}

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButtonPollType("ФИО")
    item2 = types.KeyboardButtonPollType("Адрес")
    item3 = types.KeyboardButtonPollType("Работа")

    markup.add(item1)
    markup.add(item2)
    markup.add(item3)

    bot.send_message(m.chat.id, f'Здравствуйте, что вас интересует?', reply_markup=markup)


@bot.message_handler(content_types=["text"])

def handle_text(message):
    if message.text.strip() == 'ФИО':
        answer = db['ФИО']
    elif message.text.strip() == 'Адрес':
        answer = db['Адрес']
    elif message.text.strip() == 'Работа':
        answer = db['Работа']
    else:
        answer = 'Такой команды нет'

    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)








