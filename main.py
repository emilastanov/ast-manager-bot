from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, InlineQueryHandler

from config import TOKEN, ENV, TOKEN_DEV
from core import load

if __name__ == "__main__":

    token = None

    if ENV == "production":
        token = TOKEN
    elif ENV == "development":
        token = TOKEN_DEV

    app = ApplicationBuilder().token(token).build()

    load(app, "commands", CommandHandler, named=True)
    load(app, "button_handlers", CallbackQueryHandler)
    load(app, "inline_query_handlers", InlineQueryHandler)

    print("Бот запущен...")
    app.run_polling()
