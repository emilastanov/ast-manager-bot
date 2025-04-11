import asyncio

from telegram import Update
from telegram.ext import filters, ContextTypes

from models.User import UserType
from services.deep_seek.simple_answer import simple_answer
from utils.with_typing import with_typing

handler_filters = filters.TEXT & ~filters.COMMAND


@with_typing
async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    chat = update.effective_chat
    text = message.text

    if chat.type == UserType.private:
        answer = await simple_answer(text)

        await message.reply_text(answer, parse_mode="Markdown")
