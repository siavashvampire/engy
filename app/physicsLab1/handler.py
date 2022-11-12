from telegram import Update
from telegram.ext import CallbackContext

from app.physicsLab1.controller.select_class import select_class, enter_student_number


def physics_lab_1_query_handler(update: Update, context: CallbackContext) -> None:
    if context.chat_data['command'] == 'select_class':
        select_class(update, context)


def physics_lab_1_text_handler(update: Update, context: CallbackContext) -> None:
    if context.chat_data['command'] == 'enter_student_number':
        enter_student_number(update, context)
