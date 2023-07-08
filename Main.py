import logging
import telebot

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Create a new TeleBot instance with your API token
bot = telebot.TeleBot("YOUR_API_TOKEN")

# Command handler for /start
@bot.message_handler(commands=['start'])
def start(message):
    """Send a message when the command /start is issued."""
    bot.reply_to(message, """Welcome to Binance-Trending ✅

- I am a used to list tokens on Trending with (@BinanceOfficalTrending)

- To begin, make me an Admin @BSCTrendBot in your Group

- Type /add to start tracking your coin 

- Type /settings to show all available easy to use settings

- Go Premium/Ad-Free by going to Premium Settings

- Attach your telegram link 🫂 by going to the group settings

- Type /comp to view the current buy contest leaderboard

- Type /winners to view all previous buy contests winners and add TXN as proof of payment

- Type /info to view current token info and links

- Type /remove to clear settings and competitions and remove the token from chat

- MARKETING: @BinanceOfficalTrending""")

# Command handler for /help
@bot.message_handler(commands=['help'])
def help_command(message):
    """Send a message when the command /help is issued."""
    bot.reply_to(message, """Welcome to Binance-Trending ✅

- I am a used to list tokens on Trending with (@BinanceOfficalTrending)

- To begin, make me an Admin @BSCTrendBot in your Group

- Type /add to start tracking your coin 

- Type /settings to show all available easy to use settings

- Go Premium/Ad-Free by going to Premium Settings

- Attach your telegram link 🫂 by going to the group settings

- Type /comp to view the current buy contest leaderboard

- Type /winners to view all previous buy contests winners and add TXN as proof of payment

- Type /info to view current token info and links

- Type /remove to clear settings and competitions and remove the token from chat

- MARKETING: @BinanceOfficalTrending""")
                 

# Command handler for /add
@bot.message_handler(commands=['add'])
def info_command(message):
    """Send a message when the command /add is issued."""
    bot.reply_to(message, "🟢Binance Trending Bot🟢\n\n"
                          "COMING SOON!!!\n"
                          "@BinanceOfficalTrending")
    

# Command handler for /settings
@bot.message_handler(commands=['settings'])
def info_command(message):
    """Send a message when the command /settings is issued."""
    bot.reply_to(message, "🟢Binance Trending Offical Settings🟢\n\n"
                          "COMING SOON!!!\n"
                          "@BinanceOfficalTrending")
    
# Command handler for /comp
@bot.message_handler(commands=['comp'])
def info_command(message):
    """Send a message when the command /comp is issued."""
    bot.reply_to(message, "🟢Binance Trending Competition Settings🟢\n\n"
                          "COMING SOON!!!\n"
                          "@BinanceOfficalTrending")
    
# Command handler for /winners
@bot.message_handler(commands=['winners'])
def info_command(message):
    """Send a message when the command /winners is issued."""
    bot.reply_to(message, "🟢Binance Trending Buy-Content Winners🟢\n\n"
                          "COMING SOON!!!\n"
                          "@BinanceOfficalTrending")

# Command handler for /info
@bot.message_handler(commands=['info'])
def info_command(message):
    """Send a message when the command /info is issued."""
    bot.reply_to(message, "Binance Trending Bot🛍\n\n"
                          "This bot provides live updates on the trending tokens on Binance.📊\n\n"
                          "For more information, visit our channel📚 \n @BinanceOfficalTrending 🟢")
    
# Command handler for /remove
@bot.message_handler(commands=['remove'])
def info_command(message):
    """Send a message when the command /remove is issued."""
    bot.reply_to(message, "🟢Binance Trending Clear Settings and compeitions and remove token from chat🟢\n\n"
                          "COMING SOON!!!\n"
                          "@BinanceOfficalTrending")

# Handler for unknown commands
@bot.message_handler(func=lambda message: True, content_types=['text'])
def unknown_command(message):
    """Send a message when an unknown command is issued."""
    bot.reply_to(message, "Sorry, Please use a command listed under /help.")


# Function to handle errors
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_errors(message):
    """Handle errors caused by updates."""
    try:
        # Handle the message
        # You can add your error handling logic here
        pass
    except Exception as e:
        logger.warning(f'Error: {e}')

# Run the bot
bot.polling()
