from telegram import Update
from telegram.ext import CallbackContext

from app.physicsLab1.api import add_user, check_exist_user, get_user
from app.user.api import get_user as get_user_db
from time import sleep

from core.style.InlineKeyboardMarkup import get_ikm_physics_lab_1_class, get_ikm_physics_lab_1_work_list, \
    get_ikm_physics_lab_1_user_list


def start(update: Update, context: CallbackContext):
    user_data = context.user_data
    if 'user' not in user_data.keys() or user_data['user'] == '':
        user = get_user_db(user=update.effective_user)
        if user is None:
            update.message.reply_text("your are not an engy user,please start bot with command /start to join")
            return
        else:
            context.user_data['user'] = user

    user = context.user_data['user']
    set_user_to_user_data(update, context)

    chat_data = context.chat_data
    chat_data['app'] = 'physics_lab_1'

    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)

    flag = user_data['is_admin_flag']
    if flag:
        reply_markup = get_ikm_physics_lab_1_user_list()
        message = update.message.reply_text("select student who want to see his status",
                                            reply_markup=reply_markup)

        chat_data['physics_lab_1_message_id'] = message.message_id
        chat_data['command'] = 'select_user_for_detail'
        return

    flag = check_exist_user(user)
    if not flag:
        temp_message = update.message.reply_text("Hello " + user.first_name + ", Welcome to the physics lab1.")
        flag = add_user(user)
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
            update.message.reply_text("you dont have access to send pdf please contact admin")
            return
        else:
            reply_markup = get_ikm_physics_lab_1_work_list(user.user_id)
            if len(reply_markup.inline_keyboard):
                message = update.message.reply_text("please select your HW ,whose you wish to upload",
                                                    reply_markup=reply_markup)
                chat_data['command'] = 'select_work'
                chat_data['physics_lab_1_message_id'] = message.message_id
            else:
                update.message.reply_text("you add all of your work")
                reset(update, context)


def reset(update: Update, context: CallbackContext):
    chat_data = context.chat_data
    chat_data['command'] = ''
    chat_data['app'] = ''
    chat_data['data'] = ''


def set_user_to_user_data(update: Update, context: CallbackContext):
    user = get_user_db(user=update.message.from_user)
    user_data = context.user_data
    user_data['user'] = user
    user_data['user_id'] = user.user_id
    user_data['id'] = user.id
    user_data['first_name'] = user.first_name
    user_data['last_name'] = user.last_name
    user_data['username'] = user.username
    user_data['user_physics_user'] = user.user_physics_user
    user_data['user_physics_work_user'] = user.user_physics_work_user
    user_data['is_admin_flag'] = user.check_admin()
