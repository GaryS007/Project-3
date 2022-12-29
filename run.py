import random  # Imports random module for my game

from words import words  # List of words

picked_word = None  # Picks a word from words
correct = None
incorrect = []  # All incorrect guesses go here.

print("Welcome to Hangman, you have 5 chances to save your life.")
print("Good Luck! \n")


def replace_blank():
    """
    This function is designed to replace the '_'
    in the "correct" variable with the player_guess in picked_word.
    """
    for i in correct:
        print(i, end=" ")
    print()


def generate_word():
    """
    This function generates a random word.
    """
    global picked_word, correct

    picked_word = random.choice(words)
    length = len(picked_word)
    correct = ["_"] * length  # _ x length of word from picked_word

    print(f"Your random word has {length} letters")


def start_game():
    """
    Start game function
    """
    while len(incorrect) < 5:

        print("....................................")

        player_guess = input("Want to live? Then guess a letter: ")
        print()
        if len(player_guess) > 1:
            # Prevents player from entering more than 1 character at a time
            print("Please only enter 1 letter at a time.")
        elif player_guess.isalpha() is False:
            # Prevents player from entering numbers or special characters
            print("Only letters are allowed!")
        elif player_guess in incorrect or player_guess in correct:
            # Checks if player_guess is a duplicate
            print(f"You already guessed {player_guess}, try another letter.")
        elif player_guess in picked_word:
            # This if statement sets index to 0
            # and iterates through each letter within picked_word
            # Then calls the function to replace _ with player_guess
            index = 0
            for i in picked_word:
                if i == player_guess:
                    correct[index] = player_guess
                index += 1
            print(f"You guessed correct! {player_guess} is in the word \n")
            replace_blank()
            if "_" not in correct:
                # Checks if there is any underscores left in correct,
                # if no _ found, break from loop.
                print("You win, there will be no hanging today!")
                break
        else:
            # Checks if players guess is already guessed,
            # if not, append to incorrect list.
            incorrect.append(player_guess)

            print(f"{player_guess} is not in the word, try again. \n")
            print(f"Your incorrect guesses so far: {incorrect}")
            replace_blank()
            if len(incorrect) == 1:
                print(
                    "   _____ \n"
                    "  |     | \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n"
                    "You only have 4 guesses left!\n"
                )
            elif len(incorrect) == 2:
                print(
                    "   _____ \n"
                    "  |     | \n"
                    "  |     O\n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n"
                    "You only have 3 guesses left!\n"
                )
            elif len(incorrect) == 3:
                print(
                    "   _____ \n"
                    "  |     | \n"
                    "  |     O\n"
                    "  |     | \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n"
                    "Oh No, only 2 guesses left!\n"
                )
            elif len(incorrect) == 4:
                print(
                    "   _____ \n"
                    "  |     | \n"
                    "  |     O\n"
                    "  |    /|\\ \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n"
                    "Cutting it a bit close eh? 1 guess left.\n"
                )
            elif len(incorrect) == 5:
                print(
                    "   _____ \n"
                    "  |     | \n"
                    "  |     O \n"
                    "  |    /|\\ \n"
                    "  |    / \\ \n"
                    "__|__\n"
                )
                print("RIP, better luck next time!")
                print(f"The word was '{picked_word}'")
                restart = input("Play again y/n?: ").lower()
                if restart.startswith("y"):
                    incorrect.clear()
                    correct.clear()
                    generate_word()
                else:
                    print("Thank you for playing.")
                    break
                # If the length of incorrect is equal to 5, game over.


generate_word()
start_game()
