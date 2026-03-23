from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import config

# Welcome Message
WELCOME_TEXT = """
👋 Welcome to ANIVOID Family!

📜 *GC Rules...*

• NO SPAM.🚫  
• NO RELIGION FIGHT.❌  
• UNLIMITED FUN.🐣  
• BE INCLUSIVE.❗  
• ABUSE (within limits).😋  
• 3 days inactive = remove 👺  
• NO ARGUMENTS WITH ADMINS 😄  
• Girls respect karna jaruri hai 💯  

🌌 *ADMIN RECRUITMENT* 🌌

Love anime? Want to help grow community? 🚀  

📌 Responsibilities:
➤ Add Members  
➤ Solve Issues  
➤ Collect Anime Requests  
➤ Share Links (sometimes)  

✅ Requirements:
✔ Active  
✔ Respectful  
✔ Team player  
✔ Anime lover 🎌  

📩 Message admin to apply!
"""

# Buttons (Your Groups)
def get_buttons():
    keyboard = [
        [InlineKeyboardButton("ANIVOID", url="https://t.me/+mkZFEP8IJOBkYzZl")],
        [InlineKeyboardButton("ANIVOID LIVE", url="https://t.me/+9hWGVn28gnw0NWRl")],
        [InlineKeyboardButton("ANIVOID H", url="https://t.me/+rlBl0CDkc4cwNzA1")],
        [InlineKeyboardButton("ANIVOID LINKS", url="https://t.me/+YW7SVCabCCwyMmZl")],
        [InlineKeyboardButton("ANIVOID LIVE +", url="https://t.me/+6km_RZFxdjUzNjBl")],
    ]
    return InlineKeyboardMarkup(keyboard)

# Auto Welcome when new member joins
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            text=WELCOME_TEXT,
            reply_markup=get_buttons(),
            parse_mode="Markdown"
        )

# Main function
def main():
    app = Application.builder().token(config.BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
