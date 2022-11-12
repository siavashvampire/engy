from pathlib import Path

from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

from app.time.time import time, jtime

parent_path = Path(__file__).resolve().parent


def query_handler(update: Update, context: CallbackContext) -> None:
    pass
    # if context.chat_data['command'] == 'density':
    #     density_set_density(update, context)
    # elif context.chat_data['command'] == 'set_idea_stl_file_Q':
    #     idea_stl_file_question(update, context)
    # elif context.chat_data['command'] == 'set_idea_set_overview':
    #     set_idea_accepted_idea(update, context)
    # elif context.chat_data['command'] == 'set_idea_same_innovator':
    #     set_idea_same_innovator(update, context)
    # elif context.chat_data['command'] == 'set_idea_change_user_idea':
    #     set_idea_change_user_idea(update, context)
    # elif context.chat_data['command'] == 'set_idea_insert_stl_file':
    #     set_idea_insert_stl_file(update, context)


def text_handler(update: Update, context: CallbackContext) -> None:
    chat_data = context.chat_data
    command = update.message.text
    command = str(command).lower()
    if 'command' not in chat_data.keys() or chat_data['command'] == '':
        if command == 'time':
            time(update, context)
            return
        elif command == 'jtime':
            jtime(update, context)
            return
        update.message.reply_text("command not set")
        return
    # elif chat_data['command'] == 'set_idea_input_description':
    #     set_idea_input_description(update, context)
    # elif chat_data['command'] == 'set_idea_input_innovator':
    #     set_idea_input_innovator(update, context)
    # elif chat_data['command'] == 'set_idea_change_user_idea_start':
    #     set_idea_change_user_idea_start(update, context)
    # elif context.chat_data['command'] == 'set_idea_input_stl_link':
    #     set_idea_input_stl_link(update, context)
    # elif context.chat_data['command'] == 'set_idea_overview':
    #     set_idea_overview(update, context)


def audio_handler(update: Update, context: CallbackContext):
    import speech_recognition as sr
    import pydub
    import os

    r = sr.Recognizer()
    audio = update.message.voice
    path = '../app/time/junk/'
    if not os.path.exists(parent_path.joinpath(path)):
        os.makedirs(parent_path.joinpath(path))
    path_temp = parent_path.joinpath(path + "test.ogg")
    file = audio.get_file()
    file = file.download(str(path_temp))

    # pydub.AudioSegment.ffmpeg = "F:/siavash sepahi/engy/core/FFmpeg/bin/ffmpeg.exe"
    # pydub.AudioSegment.converter = "F:/siavash sepahi/engy/core/FFmpeg/bin/ffmpeg.exe"
    ogg_version = pydub.AudioSegment.from_ogg(str(path_temp))
    path_temp2 = str(parent_path.joinpath(path + "test.wav"))
    ogg_version.export(path_temp2, format="wav")

    with sr.AudioFile(str(path_temp2)) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        try:
            command = r.recognize_google(audio_data)
        except:
            update.message.reply_text("we can not recognize what you said")
            return
    command = str(command).lower()
    os.remove(str(path_temp))
    os.remove(str(path_temp2))
    if command in ['jtime', 'persian time'] or ('jtime' in command or 'persian time' in command):
        jtime(update, context)
        return
    if command in ['time'] or 'time' in command:
        time(update, context)
        return
    update.message.reply_text(command)


def photo_handler(update: Update, context: CallbackContext):
    pass
    # chat_data = context.chat_data
    # if 'command' not in chat_data.keys() or chat_data['command'] == '':
    #     update.message.reply_text("command not set")
    #     return
    # elif chat_data['command'] == 'set_idea_upload_picture':
    #     set_idea_upload_picture(update, context)
    #
    # elif chat_data['command'] == 'set_accounting_upload':
    #     set_accounting_upload_picture(update, context)
    # else:
    #     update.message.reply_text("command that set is wrong")
    #     return


def pdf_handler(update: Update, context: CallbackContext):
    pass
    # chat_data = context.chat_data
    # if 'command' not in chat_data.keys() or chat_data['command'] == '':
    #     update.message.reply_text("command not set")
    #     return
    # elif chat_data['command'] == 'set_accounting_upload':
    #     set_accounting_upload_pdf_file(update, context)
    # else:
    #     update.message.reply_text("command that set is wrong")
    #     return


def all_handler(update: Update, context: CallbackContext):
    pass
    # chat_data = context.chat_data
    # if 'command' not in chat_data.keys() or chat_data['command'] == '':
    #     update.message.reply_text("command not set")
    #     return
    # elif 'set_accounting' in chat_data['command']:
    #     set_accounting_main_node.position.function(update, context)
