from telegram import Update
from telegram.ext import CallbackContext


from app.user.api import add_user, check_exist_user, get_user
from time import sleep

def start(update: Update, context: CallbackContext):
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    user = update.message.from_user
    temp_message = update.message.reply_text("Hello " + user.first_name + ", Welcome to the Engy.")

    flag = check_exist_user(user)

    if not flag:
        flag = add_user(user)
        sleep(1)
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=temp_message.message_id)
        if flag:
            update.message.reply_text("You have been added to Engy users correctly")
            context.user_data['user'] = get_user(user=user)
        else:
            update.message.reply_text("Sorry ,we cant add you to Engy users")
    else:
        update.message.reply_text("your already are engy user")
