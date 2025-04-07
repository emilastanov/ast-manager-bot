from uuid import uuid4

from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ContextTypes

from cases.calc_price import calc_price
from texts.calc_price import CALC_PRICE_TEXT


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

        text = CALC_PRICE_TEXT.format(
            cloth_type=cloth_type.title(),
            minutes=minutes,
            total=total,
            minimum=minimum,
            recommended=recommended
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
                input_message_content=InputTextMessageContent(f"❌ {str(e)}")
            )
        ])

    except KeyError as e:
        await update.inline_query.answer([
            InlineQueryResultArticle(
                id=str(uuid4()),
                title="❌ Ошибка: неверный ввод",
                input_message_content=InputTextMessageContent("❌ Доступные значения: Футболка, Кепка, Свитшот, Толстовка, Худи!")
            )
        ])
