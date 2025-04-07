from telegram import Update
from telegram.ext import ContextTypes

from commands.parse_args import parse_args
from config import PAGINATION_PER_PAGE
from crud.find_user import find_user
from crud.get_user_list_with_pagination import get_user_list_with_pagination
from keyboards.pagination_keyboard import get_keyboard
from utils.format_user_list_message import format_user_list_message


async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    message = update.message

    user_data = find_user(chat)

    if not user_data.is_admin:
        await message.reply_text("Недостаточно прав")

    else:
        args = parse_args("/users", message.text)
        limit = args.get("-l") or PAGINATION_PER_PAGE
        users, pagination_data = get_user_list_with_pagination(limit, 1)

        try:
            await message.reply_html(
                format_user_list_message(users, pagination_data),
                reply_markup=get_keyboard("User", pagination_data)
            )
        except ValueError as e:
            await message.reply_text(
                f"❌ Ошибка {str(e)}.",
            )

