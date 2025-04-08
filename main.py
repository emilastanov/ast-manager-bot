from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, InlineQueryHandler, MessageHandler

from config import TOKEN, ENV, TOKEN_DEV
from core import load_module

if __name__ == "__main__":

    token = None

    if ENV == "production":
        token = TOKEN
    elif ENV == "development":
        token = TOKEN_DEV

    app = ApplicationBuilder().token(token).build()

    load_module(app, "commands", CommandHandler, named=True)
    load_module(app, "button_handlers", CallbackQueryHandler, pattern=True)
    load_module(app, "inline_query_handlers", InlineQueryHandler)
    load_module(app, "other_handlers", MessageHandler, filters=True)

    print("Бот запущен...")
    app.run_polling()
