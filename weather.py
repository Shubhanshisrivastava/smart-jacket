import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6255682680:AAHI4t3sjECYrO_WDRCpcAL2SYcWgBXjOT0'

# Replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual API key
API_KEY = 'd3df2905db0854e989b1ec64b618da96'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'



# Create an updater and dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
# dispatcher.add_handler(MessageHandler(Filters.location, "ok"))

# Define the weather command
def weather(update: Update, context: CallbackContext) -> None:
    # Get the user's location from the message
    chat_id = update.message.chat_id
    user_location = (update.message.location,{"latitude":"28.575600","longitude":"77.220300"})
    print(user_location,"46251652615261562")

    if user_location:
        # Retrieve weather information based on user's location
        lat = ("28.575600")
        lon = ("77.220300")
        weather_data = get_weather_data(lat, lon)

        # Send the weather update to the user
        update.message.reply_text(f"🌦️ Weather Update:\n{weather_data}")
    else:
        update.message.reply_text("Please share your location so I can provide accurate weather yuyiyiyiiyiyiyiy.")


# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#       lat = message.text
#       print(lat,"jlsjlajsjasjauwyqwy7q65w76q")


# Function to fetch weather data from OpenWeatherMap API
def get_weather_data(latitude, longitude):
    params = {
        'lat': latitude,
        'lon': longitude,
        'appid': API_KEY,
        'units': 'metric'  # You can change to 'imperial' for Fahrenheit
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return f"The current temperature is {temperature}°C. {description.capitalize()}."
    else:
        return "Unable to fetch weather data. Please try again later."

# Add command handler
weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(weather_handler)

# Start the bot
updater.start_polling()
updater.idle()
