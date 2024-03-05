import telebot
from pymongo import MongoClient
from datetime import datetime

token ='7105847066:AAHCGAaPVV9KlC3McLFIeV_OXn3F-VnszzI'
bot = telebot.TeleBot(token)

MONGO_URI = 'mongodb+srv://awexeoz:pass321@cluster0.hzrcueu.mongodb.net/'
DATABASE_NAME = 'test'
COLLECTION_NAME = 'message'

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

@bot.message_handler(content_types=["text"])
def repeat_message(message):
    collection.insert_one({
        'message':message.text,
        'date': datetime.now() 
    })
    bot.send_message(message.chat.id,"Stratton bot " + message.text)

if __name__ == '__main__':
    bot.infinity_polling()
