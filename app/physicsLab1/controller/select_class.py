from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from app.physicsLab1.api import get_user
from app.physicsLab1.main import reset
from core.config.database import admin_id
from core.style.InlineKeyboardMarkup import ikm_accept_reject


def select_class(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_data = context.chat_data
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=chat_data['physics_lab_1_message_id'])
    user = get_user(user=update.effective_user)
    user.change_class(int(query.data))
    user = get_user(user=update.effective_user)
    message = update.effective_message.reply_text(
        "You have been added to physics lab1 class correctly,\nYou are addded in " + user.class_rel.class_name +
        "\nplease enter your student number")

    chat_data['command'] = 'enter_student_number'
    chat_data['physics_lab_1_message_id'] = message.message_id
    query.answer()
    pass


def enter_student_number(update: Update, context: CallbackContext):
    chat_data = context.chat_data
    data = update.message.text
    try:
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=chat_data['physics_lab_1_message_id'])
    except:
        pass

    try:
        data = int(data)
    except:
        message = update.message.reply_text("student code that you entered is wrong :" + data + "\nplease try again")
        chat_data['physics_lab_1_message_id'] = message.message_id
        return

    user = get_user(user=update.effective_user)
    user.change_student_number(data)
    message = update.message.reply_text(
        "Your student number is " + str(user.student_number) + "\n sending your profile to admin for accept")

    reset(update, context)

    keyboard = [
        [
            InlineKeyboardButton("accept", callback_data="physics_lab_1_" + str(user.user_rel.id) + "_accept"),
            InlineKeyboardButton("reject", callback_data="physics_lab_1_" + str(user.user_rel.id) + "_reject"),
        ]
    ]

    ikm_accept_reject = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(admin_id,
                             "user with first name " + user.user_rel.first_name + "\nclass :" + user.class_rel.class_name + "\n student number :" + str(
                                 user.student_number) + "\n user = @" + user.user_rel.username,
                             reply_markup=ikm_accept_reject)
    # TODO:bayad bezane ki payam dadeo ina v dokme vase acceptesh bede
