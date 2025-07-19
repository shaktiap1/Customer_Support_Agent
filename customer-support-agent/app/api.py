from .chatbot import generate_response
from .sentiment import analyze_sentiment

def process_message(user_input):
    sentiment = analyze_sentiment(user_input)
    bot_reply = generate_response(user_input)
    return bot_reply, sentiment
