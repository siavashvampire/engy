from telegram import Update
from telegram.ext import CallbackContext

from app.physicsLab1.api import add_user, check_exist_user, get_user
from time import sleep

from core.style.InlineKeyboardMarkup import get_ikm_physics_lab_1_class, get_ikm_physics_lab_1_work_list


def start(update: Update, context: CallbackContext):
    chat_data = context.chat_data
    chat_data['app'] = 'physics_lab_1'
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    user = update.message.from_user
    flag = check_exist_user(user)
    if not flag:
        temp_message = update.message.reply_text("Hello " + user.first_name + ", Welcome to the physics lab1.")

        flag = add_user(user)
        # flag = True
        sleep(1)
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=temp_message.message_id)

        if flag:
            message = update.message.reply_text(
                "You have been added to physics lab1 users correctly,\nplease select your class",
                reply_markup=get_ikm_physics_lab_1_class())
            chat_data['command'] = 'select_class'
            chat_data['physics_lab_1_message_id'] = message.message_id
        else:
            update.message.reply_text("Sorry ,we cant add you to physics lab1 users")
    else:
        user = get_user(user=user)
        flag = user.check_access()
        if not flag:
            update.message.reply_text("you dont have access to send pdf plz contact admin")
            return
        else:
            flag = user.check_admin()

            if not flag:
                reply_markup = get_ikm_physics_lab_1_work_list(user.user_id)
                if len(reply_markup.inline_keyboard):
                    message = update.message.reply_text("please select your HW ,whose you wish to upload",
                                                        reply_markup=reply_markup)
                    chat_data['command'] = 'select_work'
                    chat_data['physics_lab_1_message_id'] = message.message_id
                else:
                    message = update.message.reply_text("you add all of your work")
                    reset(update,context)



def reset(update: Update, context: CallbackContext):
    chat_data = context.chat_data
    chat_data['command'] = ''
    chat_data['app'] = ''
    chat_data['data'] = ''
