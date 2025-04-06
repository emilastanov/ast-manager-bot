from telegram import Update
from telegram.ext import ContextTypes

from crud.find_or_create_user import find_or_create_user
from texts.hello import HELLO, GROUP_HELLO, USER_INFO, GROUP_INFO


async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    message = update.message

    user_data, is_new = find_or_create_user(chat, message)

    text = ""

    if chat.type == "private":
        user = update.effective_user

        if is_new:
            text = HELLO

        text += USER_INFO.format(user_id=user.id, chat_id=chat.id, username=user.username)

        await message.reply_html(text)
    else:
        thread_id_info = "Не применимо"
        if message.message_thread_id:
            thread_id_info = message.message_thread_id

        if is_new:
            text = GROUP_HELLO

        text += GROUP_INFO.format(chat_title=chat.title, chat_id=chat.id, chat_type=chat.type, thread_id_info=thread_id_info)
        await message.reply_html(text)
