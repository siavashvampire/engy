from telegram import Update
from telegram.ext import CallbackContext

from app.physicsLab1.api import add_user
from time import sleep

from core.style.InlineKeyboardMarkup import ikm_physics_lab_1_class


def start(update: Update, context: CallbackContext):
    chat_data = context.chat_data
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    user = update.message.from_user
    temp_message = update.message.reply_text("Hello " + user.first_name + ", Welcome to the physics lab1.")

    flag = add_user(user)
    # flag = True
    sleep(1)
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=temp_message.message_id)
    chat_data['app'] = 'physics_lab_1'

    if flag:
        message = update.message.reply_text(
            "You have been added to physics lab1 users correctly,\nplease select your class",
            reply_markup=ikm_physics_lab_1_class)
        chat_data['command'] = 'select_class'
        chat_data['physics_lab_1_message_id'] = message.message_id
    else:
        update.message.reply_text("Sorry ,we cant add you to physics lab1 users")


def reset(update: Update, context: CallbackContext):
    chat_data = context.chat_data
    chat_data['command'] = ''
    chat_data['app'] = ''
