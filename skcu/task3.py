import telebot
token = '7105847066:AAHCGAaPVV9KlC3McLFIeV_OXn3F-VnszzI'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types = ["text"])
def repeat_message(message):
    bot.send_message(message.chat.id,"Stratton bot " + message.text)

if __name__ == '__main__':
    bot.infinity_polling()
