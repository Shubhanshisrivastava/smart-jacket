import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6255682680:AAHI4t3sjECYrO_WDRCpcAL2SYcWgBXjOT0'

# Create an updater and dispatcher
updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

# Define the start command
def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(f"Welcome, {user}! This is your bot. Type /help to see available commands.")

# Add command handler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Start the bot
updater.start_polling()
updater.idle()
