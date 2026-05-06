import re

# Intent-response pairs (customer service bot)
INTENTS = {
    r"(hello|hi|hey)":
        "Hello! Welcome to our support. How can I help you today?",
    r"(order|track|shipping)":
        "Please provide your order ID and I'll track it for you.",
    r"(refund|return|money back)":
        "Refunds are processed within 5-7 business days. "
        "Would you like to initiate a refund?",
    r"(price|cost|how much)":
        "Our plans start at ₹499/month. "
        "Visit /pricing for full details.",
    r"(bye|goodbye|exit|quit)":
        "Thank you for contacting us. Goodbye!",
}
DEFAULT = "I'm sorry, I didn't understand that. Could you rephrase?"

def get_response(user_input):
    text = user_input.lower().strip()
    for pattern, reply in INTENTS.items():
        if re.search(pattern, text):
            return reply
    return DEFAULT

def run_chatbot():
    print("Bot: Hi! I'm your support assistant. (type 'quit' to exit)")
    while True:
        user = input("You: ")
        response = get_response(user)
        print(f"Bot: {response}")
        if re.search(r"bye|quit|exit", user.lower()):
            break

run_chatbot()