"""
Key Password Generator
This program:
- Asks the user for the desired password length.
- Generates a secure password containing:
    - Uppercase letters
    - Lowercase letters
    - Digits
    - Special characters
- Uses the random module for randomness.
"""

import random
import string  # Contains predefined sets of characters

def generate_password(length):
    if length < 4: # Generates a secure password of the given length.
        return "Password length must be at least 4."

    # Character sets
    upper = string.ascii_uppercase   # A-Z
    lower = string.ascii_lowercase   # a-z
    digits = string.digits           # 0-9
    special = string.punctuation     # Special symbols like !@#$%

    # Ensure the password has at least one of each type
    password_chars = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the remaining length with random characters from all sets
    all_chars = upper + lower + digits + special
    password_chars += random.choices(all_chars, k=length - 4)

    random.shuffle(password_chars) # Shuffle the result to avoid predictable order
    return ''.join(password_chars) # Join list into a string

length = int(input("Enter desired password length: "))
print("Generated secure password:", generate_password(length))
