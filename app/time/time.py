from datetime import datetime

from jdatetime import datetime as jdatetime
from telegram import Update
from telegram.ext import CallbackContext


def time(update: Update, context: CallbackContext) -> None:
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    update.message.reply_text(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))


def jtime(update: Update, context: CallbackContext) -> None:
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    update.message.reply_text(jdatetime.now().strftime("%Y/%m/%d %H:%M:%S"))
