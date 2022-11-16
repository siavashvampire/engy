from datetime import datetime

import jdatetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from app.physicsLab1.api import get_user, get_work_list_by_id, get_work_by_user_id
from app.user.api import get_user as get_user_db
from app.physicsLab1.main import reset
from core.config.database import admin_id
from core.handler import download_document


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


def select_work(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_data = context.chat_data
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=chat_data['physics_lab_1_message_id'])
    work = get_work_list_by_id(int(query.data))
    message = update.effective_message.reply_text(
        "You have been selected work " + work.work_name + "\nplease enter your pdf")

    chat_data['command'] = 'enter_work_pdf'
    chat_data['data'] = int(query.data)
    chat_data['physics_lab_1_message_id'] = message.message_id
    query.answer()


def select_user_for_detail(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_data = context.chat_data
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=chat_data['physics_lab_1_message_id'])
    works = get_work_by_user_id(int(query.data))
    user = get_user_db(user_id=int(query.data))
    text = user.first_name + " " + str(user.id) + "\n" * 3
    for work in works:
        text += work.work.work_name + ":\n" + str(jdatetime.datetime.fromgregorian(
            datetime=datetime.strptime(str(works[0].date_time),
                                       "%Y-%m-%d %H:%M:%S"))) + "\n" + "------------------" + "\n" * 2
    message = update.effective_message.reply_text(
        text)
    reset(update, context)
    query.answer()


def enter_work_pdf(update: Update, context: CallbackContext):
    chat_data = context.chat_data
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=chat_data['physics_lab_1_message_id'])
    message = update.effective_message.reply_text("downloading your work ...")
    user = get_user(user=update.effective_user)
    path = download_document(update.message.document, '../app/physicsLab1/HW/HW_' + str(chat_data['data']) + '/',
                             str(user.user_rel.id) + '.pdf')
    path = download_document(update.message.document, '../app/physicsLab1/HW/' + str(user.user_rel.id) + '/',
                             'HW_' + str(chat_data['data']) + '.pdf')

    work = get_work_list_by_id(chat_data['data'])
    work.insert_data(user.user_rel.id)
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=message.message_id)
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)
    update.effective_message.reply_text("Your work for " + work.work_name + " has been uploaded")

    reset(update, context)


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
    update.message.reply_text(
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
