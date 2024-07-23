import json
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Load configuration
with open('config.json', 'r') as f:
    config = json.load(f)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define the start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(config['quizBot']['messages']['welcome'])

# Define the error handler
def error(update: Update, context: CallbackContext) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    if update.message:
        update.message.reply_text(config['quizBot']['messages']['error'])
    else:
        logger.error('No message found in update.')

# Main function to start the bot
def main() -> None:
    # Create the Updater and pass it your bot's token
    # Make sure to replace 'YOUR_TOKEN_HERE' with your actual token
    with open('config.json', 'r') as f:
        config = json.load(f)
    token = config.get('token', 'YOUR_TOKEN_HERE')
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Register the error handler
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
