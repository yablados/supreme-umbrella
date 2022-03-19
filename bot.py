from telegram.ext import Updater
from telegram.ext import CommandHandler

def sms(bot, update):
    print("Кто-то отправил команду /start. Что мне делать ?")
    bot.message.reply_text('Здраствуйте, я бот! \nЯ пока не умею разговаривать, но я быстро учусь!')

def main():
    my_bot = Updater("5252643142:AAHDdbzArzBqVCejtAYjL2nHAk3zPImAvJQ", "https://telegg.ru/orig/bot", use_context=True)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))

    my_bot.start_polling()
    my_bot.idle()
main()