import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6255682680:AAHI4t3sjECYrO_WDRCpcAL2SYcWgBXjOT0'

# Dictionary of emergency contacts
emergency_contacts = {
    'Police': '911',
    'Fire Department': '112',
    'Medical Emergency': '999',
    'Family Contact': '+123456789'
}

# Create an updater and dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define the emergency command
def emergency(update: Update, context: CallbackContext) -> None:
    contact_list = "\n".join([f"{contact}: {number}" for contact, number in emergency_contacts.items()])
    update.message.reply_text(f"🚨 Emergency Contacts:\n{contact_list}")

# Add command handler
emergency_handler = CommandHandler('emergency', emergency)
dispatcher.add_handler(emergency_handler)

# Start the bot
updater.start_polling()
updater.idle()
