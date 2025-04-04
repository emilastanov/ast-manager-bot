from uuid import uuid4

from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ContextTypes

from cases.calc_price import calc_price


async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query

    if not query:
        return

    parts = query.strip().split()

    if len(parts) != 2:
        await update.inline_query.answer([
            InlineQueryResultArticle(
                id=str(uuid4()),
                title="❌ Ошибка: Введите тип и время (мин)",
                input_message_content=InputTextMessageContent("Формат: <тип> <время в минутах>")
            )
        ])
        return

    cloth_type, time_str = parts
    try:
        minutes = int(time_str)
        total, minimum, recommended = calc_price(minutes, cloth_type)
        title = f"{cloth_type.title()} • {minutes} мин"
        text = (
            f"🧵 Стоимость вышивки:\n\n"
            f"• Тип одежды: {cloth_type.title()}\n"
            f"• Время: {minutes} минут\n"
            f"• Себестоимость: {total} ₽\n"
            f"• Минимальная цена: {minimum} ₽\n"
            f"• 💡 Рекомендованная цена: {recommended} ₽"
        )

        await update.inline_query.answer([
            InlineQueryResultArticle(
                id=str(uuid4()),
                title=title,
                input_message_content=InputTextMessageContent(text)
            )
        ])

    except ValueError as e:
        await update.inline_query.answer([
            InlineQueryResultArticle(
                id=str(uuid4()),
                title="❌ Ошибка: неверный ввод",
                input_message_content=InputTextMessageContent(str(e))
            )
        ])
