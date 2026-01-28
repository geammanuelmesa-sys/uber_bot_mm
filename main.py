from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot de análisis Uber RD\n\n"
        "Envíame los datos así:\n"
        "ingreso,km,minutos\n\n"
        "Ejemplo:\n700,12,25"
    )

def analizar_viaje(ingreso, km, minutos):
    gkm = ingreso / km
    gh = ingreso / minutos * 60

    if gkm >= 40 and gh >= 500:
        estado = "🟢 EXCELENTE"
    elif gkm >= 30:
        estado = "🟡 REGULAR"
    else:
        estado = "🔴 MALO"

    return gkm, gh, estado

async def mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        texto = update.message.text.replace(" ", "")
        ingreso, km, minutos = map(float, texto.split(","))

        gkm, gh, estado = analizar_viaje(ingreso, km, minutos)

        await update.message.reply_text(
            f"📊 Resultado\n\n"
            f"💰 RD${ingreso}\n"
            f"📏 {km} km\n"
            f"⏱ {minutos} min\n\n"
            f"📈 RD${gkm:.2f} / km\n"
            f"⏰ RD${gh:.2f} / hora\n\n"
            f"{estado}"
        )
    except:
        await update.message.reply_text("❌ Formato incorrecto. Usa: 700,12,25")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensaje))
    app.run_polling()

if __name__ == "__main__":
    main()



