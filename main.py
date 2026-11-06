import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📺 Promosi YouTube"],
        ["💰 Daftar Harga"],
        ["📦 Status Pesanan"],
        ["ℹ️ Bantuan"]
    ]

    await update.message.reply_text(
        "🚀 SELAMAT DATANG DI SUBPRO AI!\n\n"
        "Layanan promosi digital YouTube.\n"
        "Silakan pilih menu:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard, resize_keyboard=True
        )
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📺 Promosi YouTube":
        await update.message.reply_text(
            "Silakan kirim link channel YouTube kamu."
        )

    elif text == "💰 Daftar Harga":
        await update.message.reply_text(
            "Daftar layanan:\n"
            "1. Promosi channel\n"
            "2. Pembuatan video Shorts\n"
            "3. Desain thumbnail\n\n"
            "Harga dikonfirmasi oleh admin."
        )

    elif text == "📦 Status Pesanan":
        await update.message.reply_text(
            "Silakan hubungi admin untuk mengecek pesanan."
        )

    elif text == "ℹ️ Bantuan":
        await update.message.reply_text(
            "SUBPRO AI siap membantu kebutuhan promosi digital kamu."
        )

    elif "youtube.com" in text or "youtu.be" in text:
        await update.message.reply_text(
            "✅ Link diterima!\n"
            "Pesanan akan diteruskan ke admin untuk diperiksa."
        )

    else:
        await update.message.reply_text(
            "Silakan pilih menu yang tersedia."
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

    print("SUBPRO AI berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
