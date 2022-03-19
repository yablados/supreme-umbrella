from telegram.ext import Updater

def main():
    my_bot = Updater("5252643142:AAHDdbzArzBqVCejtAYjL2nHAk3zPImAvJQ", "https://telegg.ru/orig/bot", use_context=True)
    my_bot.start_polling()
    my_bot.idle()
main()