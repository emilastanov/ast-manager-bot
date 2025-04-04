from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, InlineQueryHandler

from config import TOKEN
from core import load

if __name__ == "__main__":

    app = ApplicationBuilder().token(TOKEN).build()
    load(app, "commands", CommandHandler, named=True)
    load(app, "button_handlers", CallbackQueryHandler)
    load(app, "inline_query_handlers", InlineQueryHandler)

    print("Бот запущен...")
    app.run_polling()
