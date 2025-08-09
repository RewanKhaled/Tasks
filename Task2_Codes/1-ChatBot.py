"""
Chatلآot
This program:
- Asks the user for their name and remembers it during the session.
- Can answer a few basic questions.
- Can do simple addition and subtraction (without using libraries).
- Gives a default reply if it doesn't know the answer.
- All data is stored in memory (no files are used).
"""

import re
import random

print("=" * 50)
print("WELCOME TO REWAN'S CHATBOT PROGRAM".center(50))
print("=" * 50)

user_data = {} # Store user data (name, etc.)

# known responses
responses = {
    "nice": "Great! How can i help you today?",
    "hi": "Hi there! How are you?",
    "how are you": "I'm just a ChatBot, but i'm doing great! How about you?"
}

# Random fallback messages
fallbacks = [
    "I'm not sure about that.",
    "Hmm... I don't have that answer yet.",
    "Can you try asking me in another way?",
    "That's interesting! But I don't know the answer.",
    "I'll have to think about that one."
]

while True:
    # If name not yet saved, ask for it once
    if "name" not in user_data:
        name = input("ChatBot: Hey! What's your name?\nYou: ")
        user_data["name"] = name
        print(f"ChatBot: Nice to meet you, {name}!")
        continue

    user_input = input("You: ").lower().strip()  # Get user input

    # Exit commands
    if user_input in ["bye", "exit", "quit"]:
        print(f"ChatBot: Bye {user_data['name']}! Have a great day!")
        break
    
    # Thank you replies
    if user_input in ["thank you", "thanks", "thx", "thank u"]:
        print("ChatBot: You're welcome!")
        continue

    # greetings
    if user_input in responses:
        print("ChatBot:", responses[user_input])
        continue

    # remove punctuation except math symbols
    numbers = re.findall(r"-?\d+\.?\d*", user_input)
    if len(numbers) >= 2:
        num1, num2 = map(float, numbers[:2]) # handles integers and decimals
        # Addition
        if "add" in user_input or "+" in user_input:
            print("ChatBot: The sum is", num1 + num2)
            continue
        # Subtraction
        elif "subtract" in user_input or "-" in user_input:
            parts = user_input.replace(" ", "").split("-")
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
              num1, num2 = map(int, parts)
              print(f"ChatBot: The difference is {num1 - num2}")
              continue
        #  Multiplication
        elif "multiply" in user_input or "*" in user_input:
            print("ChatBot: The product is", num1 * num2)
            continue
        # Division
        elif "divide" in user_input or "/" in user_input:
            if num2 != 0:
                print("ChatBot: The quotient is", num1 / num2)
            else:
                print("ChatBot: I can't divide by zero!")
            continue

    # Unknown input → random fallback
    print(f"ChatBot: {random.choice(fallbacks)}")