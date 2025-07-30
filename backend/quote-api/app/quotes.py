import random

QUOTES = [
    "Stay hungry, stay foolish.",
    "Talk is cheap. Show me the code.",
    "First, solve the problem. Then, write the code.",
    "Simplicity is the soul of efficiency.",
    "Code is like humor. When you have to explain it, it’s bad."
]

def get_random_quote():
    return random.choice(QUOTES)