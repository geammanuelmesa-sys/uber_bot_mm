from telegram.ext import ApplicationBuilder, CommandHandler
import os

TOKEN = os.getenv("TOKEN")

async def start(update, context):
    await update.message.reply_text("¡Bot activo! 🚀")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("🤖 Bot iniciado, esperando mensajes...")

    app.run_polling()

if __name__ == "__main__":
    main()
