import telebot

bot = telebot.TeleBot("1847079990:AAFrCKmrWELRCmRtYG-PnEAhPK7k_qr1DrU")

@bot.message_handler(content_types=['text'])
def send_welcome(message):

#Отвечает на сообщение сообщением (Forward).
	bot.reply_to(message, message.text)
#Дублирует сообщение.
    #bot.send_message(message.chat.id, message.text )
bot.polling( none_stop = True) 