from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

TOKEN = '7624021359:AAGoDzEYgnBcVjlTf_RBYatJxgdNH4D-pd4'

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Перейти в WebApp", url="https://yourwebsite.com")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Нажмите на кнопку для открытия WebApp', reply_markup=reply_markup)

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    
    application.run_polling()

if __name__ == "__main__":
    main()
