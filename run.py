import random

words = ["orange", "apple"]  # List of words

picked_word = random.choice(words)  # Picks a word from words
length = len(picked_word)

print(f"Your random word has {length} letters")

correct = ["_"] * length  # _ x length of word from picked_word
incorrect = []  # All incorrect guesses go here.


def replace_blank():
    """
    This function is designed to replace the '_'
    in the "correct" variable with the player_guess in picked_word.
    """
    for i in correct:
        print(i, end=" ")
    print()


while True:

    print("....................................")

    player_guess = input("Want to live? Then guess a letter: ")

    if player_guess in picked_word:
        # This if statement sets index to 0
        # and iterates through each letter within picked_word.
        # Then calls the function to replace _ with player_guess
        index = 0
        for i in picked_word:
            if i == player_guess:
                correct[index] = player_guess
            index += 1
        replace_blank()

    else:
        if player_guess not in incorrect:
            # Checks if players guess is already guessed,
            # if not, append to incorrect list.
            incorrect.append(player_guess)
            print(f"{player_guess} is not in the word, try again.")
            print(f"Your incorrect guesses so far: {incorrect}")
        else:
            print(f"You already guessed {player_guess}, try another letter.")
    if len(incorrect) == 1:
        print(
            "   _____ \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "__|__\n"
        )
    if len(incorrect) == 2:
        print(
            "   _____ \n"
            "  |     | \n"
            "  |     O\n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "__|__\n"
        )
    if len(incorrect) == 3:
        print(
            "   _____ \n"
            "  |     | \n"
            "  |     O\n"
            "  |     | \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "__|__\n"
        )
    if len(incorrect) == 4:
        print(
            "   _____ \n"
            "  |     | \n"
            "  |     O\n"
            "  |    /|\ \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "__|__\n"
        )
    if len(incorrect) == 5:
        print(
            "   _____ \n"
            "  |     | \n"
            "  |     O \n"
            "  |    /|\ \n"
            "  |    / \ \n"
            "__|__\n"
        )
        print(f"RIP, better luck next time! The word was {picked_word}")
        break
        # incorrect is a list that contains the incorrect guesses of the player
        # If the length of incorrect is equal to 5, game over.
    if "_" not in correct:
        # Checks if there is any underscores left in correct,
        # if no _ found, break from loop.
        print("You win, there will be no hanging today!")
        break
