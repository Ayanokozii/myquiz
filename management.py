from telegram.ext import ConversationHandler

# Define states
QUIZ, QUESTION, SCORE = range(3)

# Define a dictionary to keep track of user scores
user_scores = {}

# Function to start the quiz
def start_quiz(update: Update, context: CallbackContext) -> int:
    user_scores[update.message.from_user.id] = 0
    # Start with the first question
    return ask_question(update, context)

# Function to ask a question
def ask_question(update: Update, context: CallbackContext) -> int:
    question = get_random_question()
    context.user_data['answer'] = question['answer']
    update.message.reply_text(question['question'])
    return QUESTION

# Function to handle answers
def handle_answer(update: Update, context: CallbackContext) -> int:
    user_answer = update.message.text
    correct_answer = context.user_data['answer']
    if user_answer.lower() == correct_answer.lower():
        user_scores[update.message.from_user.id] += 1
        update.message.reply_text(config['quizBot']['messages']['correct'])
    else:
        update.message.reply_text(config['quizBot']['messages']['incorrect'].format(answer=correct_answer))

    return ask_question(update, context)

# Function to get a random question (placeholder, you'll need to implement this)
def get_random_question():
    # Replace this with actual question fetching logic
    return {
        "question": "What is the capital of France?",
        "answer": "Paris"
    }

# Add handlers for quiz commands
quiz_handler = ConversationHandler(
    entry_points=[CommandHandler('quiz', start_quiz)],
    states={
        QUESTION: [MessageHandler(Filters.text & ~Filters.command, handle_answer)]
    },
    fallbacks=[CommandHandler('start', start)]
)
dispatcher.add_handler(quiz_handler)
