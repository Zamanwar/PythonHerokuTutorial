from telegram.ext.updater import Updater
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import os

TOKEN = os.environ.get("TELEGRAM_ID")


def start(update, context):
    name = update.message.chat.first_name
    msg = "Hi " + name + "! Welcome."
    context.bot.send_message(update.message.chat.id, msg)


def mimic(update, context):
    context.bot.send_message(update.message.chat.id, update.message.txt)


def details(update, context):
    context.bot.send_message(update.message.chat.id, update.message)


def error(update, context):
    context.bot.send_message(update.message.chat.id, " Error !!")


def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("details", details))
    dp.add_handler(MessageHandler(Filters.text, mimic))

    dp.add_error_handler(error)
#    updater.start_webhook(listen="0.0.0.0", port=os.environ.get("PORT", 443),
#                          url_path="https://zam-isbot.herokuapp.com/" + TOKEN)
# updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
