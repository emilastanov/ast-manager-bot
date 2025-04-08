import asyncio

from telegram import Update
from telegram.ext import filters, ContextTypes

from services.deep_seek.simple_answer import simple_answer
from utils.with_typing import with_typing

handler_filters = filters.TEXT & ~filters.COMMAND


@with_typing
async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    text = message.text

    answer = await simple_answer(text)

    await message.reply_text(answer, parse_mode="Markdown")
