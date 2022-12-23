import random

words = ["orange", "apple"]  # List of words

picked_word = random.choice(words)  # Picks a word from words
blank_word = "_"*len(picked_word)
length = len(picked_word)

print(
    f"Your random word has {length} letters"
    )

correct = ['_']*len(picked_word)
incorrect = []


def replace_blank():
    """
    This function is designed to replace the '_' 
    in the "correct" variable with the player_guess in picked_word.
    """
    for i in correct:
        print(i, end='')
    print()


while True:

    print('....................................')

    player_guess = input(
        "Guess a letter: "
    )

    if player_guess in picked_word:
        index = 0
        for i in picked_word:
            if i == player_guess:
                correct[index] = player_guess
            index += 1
        replace_blank()
        
    else:
        if player_guess not in incorrect:
            incorrect.append(player_guess)
        else:
            print(f"You already guessed {player_guess}, try another letter.")
    
