from words import words
import random

def get_valid_word(words):
    words = random.choice(words)
    while "-" or " " in words:
        words = random.choice(words)

    return words

def hangman():
    words = get_valid_word(words)
    word

