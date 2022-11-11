from time import sleep
from app.gmail.gmail import Gmail

from pathlib import Path
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

from app.time.time import time, jtime
from core.database.database import create_db

from app.user.api import add_user
from core.handler import text_handler, audio_handler

parent_path = Path(__file__).resolve().parent

gmail = Gmail()


def start(update: Update, context: CallbackContext):
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    user = update.message.from_user
    temp_message = update.message.reply_text("Hello " + user.first_name + ", Welcome to the Engy.")
    flag = add_user(user)
    sleep(1)
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=temp_message.message_id)
    if flag:
        update.message.reply_text("You have been added to Engy users correctly")
    else:
        update.message.reply_text("Sorry ,we cant add you to Engy users")


if __name__ == '__main__':
    from telegram.ext import CallbackQueryHandler, Dispatcher
    from telegram.ext.updater import Updater
    from telegram.ext.commandhandler import CommandHandler
    from telegram.ext.messagehandler import MessageHandler
    from telegram.ext.filters import Filters
    # from app.density.main import den
    # from app.gcode.main import gcode, readfile
    # from app.idea.main import set_idea, add_user_idea, set_idea_upload_stl_file
    from core.config.database import telegram_token

    # from core.handler import query_handler, photo_handler, text_handler, pdf_handler, all_handler
    # from app.accounting.main import set_accounting

    updater = Updater(telegram_token, use_context=True)
    dp: Dispatcher = updater.dispatcher
    # updater.dispatcher.add_handler(MessageHandler(Filters.update, all_handler))
    # dp.add_handler()

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('time', time))
    dp.add_handler(CommandHandler('jtime', jtime))
    dp.add_handler(MessageHandler(Filters.text, text_handler))
    # updater.dispatcher.add_handler(CommandHandler('upload_gcode', gcode))
    # updater.dispatcher.add_handler(CommandHandler('set_density', den))
    # updater.dispatcher.add_handler(CommandHandler('set_idea', set_idea))
    # updater.dispatcher.add_handler(CommandHandler('set_accounting', set_accounting))
    # updater.dispatcher.add_handler(CommandHandler('add_user_idea', add_user_idea))
    # updater.dispatcher.add_handler(CallbackQueryHandler(query_handler))
    # updater.dispatcher.add_handler(MessageHandler(Filters.document.file_extension('gcode'), readfile))
    # updater.dispatcher.add_handler(MessageHandler(Filters.document.file_extension('stl'), set_idea_upload_stl_file))
    # updater.dispatcher.add_handler(MessageHandler(Filters.document.pdf, pdf_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.audio, audio_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.voice, audio_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.document.audio, audio_handler))
    # updater.dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))

    create_db()
    print('bot is running')
    updater.start_polling()
