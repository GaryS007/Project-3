import random

words = ['Orange', 'Apple']  # List of words

picked_word = random.choice(words)

player_guess = input(f'Welcome to Hangman, your word is {picked_word}\n' + 'Guess a letter: ')

print(player_guess)
