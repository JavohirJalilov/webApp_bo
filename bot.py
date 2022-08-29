from telegram.ext import Updater, CommandHandler,MessageHandler,Filters, InlineQueryHandler,CallbackQueryHandler
from telegram import WebAppInfo, ReplyKeyboardRemove, Update, InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton,InputTextMessageContent,InlineQueryResultArticle,KeyboardButton
import telegram
import json
import os

TOKEN = os.environ['TOKEN']

def start(update,context):
    text = 'Click the sign up button to register!'
    bot = context.bot 
    url="https://630c3985a0b05a52eb7bbed7--comforting-jelly-086491.netlify.app"
    # url="https://python-telegram-bot.org/static/webappbot"

    """Send a message with a button that opens a the web app."""
    update.message.reply_text(
        text=text,
        reply_markup=ReplyKeyboardMarkup.from_button(
            KeyboardButton(
                text="sign up!",
                web_app=WebAppInfo(url=url),
                colorScheme='dark'
            )
        ),
    )



def web_app_data(update, context) -> None:
    """Print the received data and remove the button."""
    # Here we use `json.loads`, since the WebApp sends the data JSON serialized string
    # (see webappbot.html)
    data = json.loads(update.effective_message.web_app_data.data)
    
    print(data)
    # update.message.reply_html(
    #     text=f"You selected the color with the HEX value <code>{data['hex']}</code>. The "
    #     f"corresponding RGB value is <code>{tuple(data['rgb'].values())}</code>.",
    #     reply_markup=ReplyKeyboardRemove(),
    # )


updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.status_update, web_app_data))

updater.start_polling()
updater.idle()