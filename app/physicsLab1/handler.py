from telegram import Update
from telegram.ext import CallbackContext

from app.physicsLab1.controller.select_class import select_class, enter_student_number, select_work, enter_work_pdf, \
    select_user_for_detail


def physics_lab_1_query_handler(update: Update, context: CallbackContext) -> None:
    if context.chat_data['command'] == 'select_class':
        select_class(update, context)
    elif context.chat_data['command'] == 'select_work':
        select_work(update, context)
    elif context.chat_data['command'] == 'select_user_for_detail':
        select_user_for_detail(update, context)
    else:
        context.bot.send_message(update.effective_user.id, "command not set")
        return


def physics_lab_1_text_handler(update: Update, context: CallbackContext) -> None:
    if context.chat_data['command'] == 'enter_student_number':
        enter_student_number(update, context)
    else:
        update.message.reply_text("command not set")
        return


def physics_lab_1_pdf_handler(update: Update, context: CallbackContext) -> None:
    if context.chat_data['command'] == 'enter_work_pdf':
        enter_work_pdf(update, context)
    else:
        update.message.reply_text("command not set")
        return
