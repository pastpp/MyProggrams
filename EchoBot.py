import telebot
import Tokens

bot = telebot.TeleBot(Tokens.EchoBot)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот который повторяет все что ему скажут.".format(message.from_user, bot.get_me()), parse_mode='html')
 


@bot.message_handler(content_types='text')
def echo_all(message):

#Ответ сообщением на сообщение(Forward)
	#bot.reply_to(message, message.text)


#Дублирует сообщение.
	bot.send_message(message.chat.id, message.text)
bot.polling(none_stop=True)