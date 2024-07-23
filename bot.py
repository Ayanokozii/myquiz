import json
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

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
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(config['quizBot']['messages']['welcome'])

# Define the error handler
async def error(update: Update, context: CallbackContext) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    if update.message:
        await update.message.reply_text(config['quizBot']['messages']['error'])
    else:
        logger.error('No message found in update.')

# Main function to start the bot
def main() -> None:
    # Create the Application and pass it your bot's token
    # Make sure to replace 'YOUR_TOKEN_HERE' with your actual token
    token = config.get('token', '7332008423:AAFExbt7RhYJZ9IhR8lFQ4IQZVYvXYiIkYs')
    application = Application.builder().token(token).build()

    # Register the start command handler
    application.add_handler(CommandHandler("start", start))

    # Register the error handler
    application.add_error_handler(error)

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
