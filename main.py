from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import config

# Simple Welcome Message
WELCOME_TEXT = "👋 Welcome to ANIVOID Family!"

# Buttons (All your groups)
def get_buttons():
    keyboard = [
        [InlineKeyboardButton("ANIVOID", url="https://t.me/+mkZFEP8IJOBkYzZl")],
        [InlineKeyboardButton("ANIVOID LIVE", url="https://t.me/+9hWGVn28gnw0NWRl")],
        [InlineKeyboardButton("ANIVOID H", url="https://t.me/+rlBl0CDkc4cwNzA1")],
        [InlineKeyboardButton("ANIVOID LINKS", url="https://t.me/+YW7SVCabCCwyMmZl")],
        [InlineKeyboardButton("ANIVOID LIVE +", url="https://t.me/+6km_RZFxdjUzNjBl")],
    ]
    return InlineKeyboardMarkup(keyboard)

# Auto Welcome
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            text=WELCOME_TEXT,
            reply_markup=get_buttons()
        )

# Run Bot
def main():
    app = Application.builder().token(config.BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
