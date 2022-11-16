from app.gmail.gmail import Gmail

from pathlib import Path

parent_path = Path(__file__).resolve().parent

gmail = Gmail()

if __name__ == '__main__':
    from core.database.database import create_db

    create_db()

    from telegram.ext import Dispatcher, CallbackQueryHandler
    from telegram.ext.updater import Updater
    from telegram.ext.commandhandler import CommandHandler
    from telegram.ext.messagehandler import MessageHandler
    from telegram.ext.filters import Filters
    from app.time.time import time, jtime
    from app.user.main import start
    from app.physicsLab1.main import start as physics_start

    from core.handler import text_handler, audio_handler, query_handler, pdf_handler
    # from app.density.main import den
    # from app.gcode.main import gcode, readfile
    # from app.idea.main import set_idea, add_user_idea, set_idea_upload_stl_file
    from core.config.database import telegram_token

    # from core.handler import query_handler, photo_handler, text_handler, pdf_handler, all_handler
    # from app.accounting.main import set_accounting

    updater = Updater(telegram_token, use_context=True)
    dp: Dispatcher = updater.dispatcher
    # updater.dispatcher.add_handler(MessageHandler(Filters.update, all_handler))

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('time', time))
    dp.add_handler(CommandHandler('jtime', jtime))
    dp.add_handler(CommandHandler('physics_lab1', physics_start))
    dp.add_handler(MessageHandler(Filters.text, text_handler))
    dp.add_handler(MessageHandler(Filters.document.pdf, pdf_handler))
    updater.dispatcher.add_handler(CallbackQueryHandler(query_handler))
    # updater.dispatcher.add_handler(MessageHandler(Filters.document.file_extension('gcode'), readfile))
    # updater.dispatcher.add_handler(MessageHandler(Filters.document.file_extension('stl'), set_idea_upload_stl_file))
    # updater.dispatcher.add_handler(MessageHandler(Filters.document.pdf, pdf_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.audio, audio_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.voice, audio_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.document.audio, audio_handler))
    # updater.dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))

    print('bot is running')
    updater.start_polling()
