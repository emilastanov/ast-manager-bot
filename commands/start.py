from telegram import Update
from telegram.ext import ContextTypes

from texts.hello import HELLO, GROUP_HELLO


async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    chat = update.effective_chat

    if update.message.chat.type == "private":
        user = update.effective_user

        text = HELLO.format(user_id=user.id, chat_id=chat.id, username=user.username)

        await message.reply_html(text)
    else:
        thread_id_info = "Не применимо"
        if message.message_thread_id:
            thread_id_info = message.message_thread_id

        text = GROUP_HELLO.format(chat_title=chat.title, chat_id=chat.id, chat_type=chat.type, thread_id_info=thread_id_info)
        await message.reply_html(text)
