import logging
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext 

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6255682680:AAHI4t3sjECYrO_WDRCpcAL2SYcWgBXjOT0'

# Health and wellness tips for soldiers
health_tips = [
    "Stay hydrated throughout the day to maintain peak performance.",
    "Prioritize quality sleep to support physical and mental well-being.",
    "Incorporate regular exercise into your routine for overall fitness.",
    "Consume a balanced diet to fuel your body and mind.",
    "Practice mindfulness and stress management techniques to enhance resilience.",
    "Stay connected with your comrades for a strong support system.",
]

# Create an updater and dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define the health command
def health(update: Update, context: CallbackContext) -> None:
    tip = random.choice(health_tips)
    update.message.reply_text(f"🌟 Health Tip for Soldiers:\n\n{tip}")

# Add command handler
health_handler = CommandHandler('health', health)
dispatcher.add_handler(health_handler)

# Start the bot
updater.start_polling()
updater.idle()