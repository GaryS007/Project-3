# Hangman Game

Hangman is a Python terminal game that can be accessed and played via Heroku. 

Players can start playing by simply guessing a letter. The player has 5 attempts to guess the word. 

[Live version of my game](https://gary-project-3.herokuapp.com/)

![Picture of my game](https://garys007.github.io/Project-3/assets/images/responsive.png)

## How to play

Hangman is a game that I've played on paper since my childhood. A word is selected by random and the amount of letters in the world is communicated to the player.
To start playing, follow the instructions by entering your first letter (guess).
The game will then let you know if your guess is correct or incorrect. 
The score of the game will be consistently communicated to the player after each incorrect guess. 
The list of incorrect guesses is displayed as well as a text based 'image' of the hangman we're all so used to seeing. 
The player can win by guessing the word within 5 guesses. 
After the player wins or loses, the game will reset and ask the player if they want to try again.

## Features

### Existing Features

* Random Word generated for each new game.
    * The amount of letters in the word is communicated to the player
    * The word is encrypted using underscores for each letter.
    * A successful guess will replace the underscore with the correct letter guessed.

![Picture of randomly generated word](https://garys007.github.io/Project-3/assets/images/random.png)

* Accepts letter inputs by the player.

![Enter your letter guess here](https://garys007.github.io/Project-3/assets/images/letter.png)

* Remaining guesses is maintained and displayed throughout the game.

![Displaying remaining guesses](https://garys007.github.io/Project-3/assets/images/guesses.png)

* Input validation and error-checking
    * You cannot enter numbers or special characters
    * You must enter letters
    * You cannot enter multiple characters at the same time
    * You cannot enter the same guess more than once

![Error handling](https://garys007.github.io/Project-3/assets/images/errors.png)

### Future Features
* Add a larger library of words
* Add differences in difficulty based on number of letters.
    * If word is less than 4 letters, only give player 3 guesses.
    * If word is larger than 10 letters, give player 6 guesses.

## Data Model
I used global variables to store the data as the player continues to play the game.

The picked_word variable will store the randomly generated word from the generate_word() function. 
The length of this word is calculated by this function and communicated to the player.
The words are extracted from a separate python file called words.py.

The correct variable stores all correct guesses made by the player. 
This allows me to check if the player already guessed a letter.
It also allows me to check if the player has won the game. Once all the _ (underscores) are replaced with a correct letter,
they win the game.

The incorrect variable tracks all incorrect guesses. The game ends when the player has a total of 5 incorrect guesses.
This also allows me to check if the player already guessed a letter.

The entire game runs on a While loop and the loop will end when total guesses reaches 5.

## User Experience

* Player is greeted with relevant messaging and instructions to play the game.
* a Random Word will be chosen so the player can start guessing.
* Player can now enter a letter into the input field.
* After guessing a letter, the player should know if their guess is right or wrong.
* After guessing a letter, the player should know how many guesses remain if they got it wrong.
* After guessing the word correctly, the player should be informed that they are victorious.
* If the player guessed the word incorrectly, they should be informed that they have lost and be told what the word was.
* The player should then be given the option to restart the game.


## Testing

I have manually tested my project throughout the entire process of building it by doing the following:
* Launch my game by using python3 run.py within Gitpod and test my game after every change.
* Test specific scenarios such as number entries, multiple character entries and duplicate inputs.
* Test using the Code Institute Heroku Terminal to check that everything is ok.

### Bugs

**Fixed Bugs**

* After I made the primary while loop for my game. When I implemented more complex code or scenarios, I inadvertenly broke my game without realising it. 
I noticed the bugs during testing and realised that my if / elif indentation was incorrect. This made me be very careful with indentation moving forward.
* I was calling the primary start_game() function within the function. I learned that this is known as recursion and should be avoided where possible. 
To solve this I removed the recursion and instead changed how the while loop works so I didn't need to call the function a second time.
* Due to how I did my Hangman drawings, Gitpod / VS Code kept giving me an error due to the \ used for the arms and legs. To fix this I had to do \\ instead of a single \.
This fix was not 100% necessary as the game functioned perfectly regardless.
* As I was about to deploy, I realised that I never added a try: except: for CTRL C, it threw an error I didn't like. 

### Remaining Bugs

* No bugs remaining.

### Validator Testing

* PEP8
    * No errors were returned from https://pep8ci.herokuapp.com/

## Deployment

This project was deployed using Heroku.

* Create a new Heroku App via Heroku Dashboard.
* Set the buildbacks to Python and NodeJS in that order.
* Link the Heroku App to the appropriate Github repository.
* Click **Deploy**

## Mock / Flowchart

Before starting with my project in Gitpod, I started writing down the steps my game would take in order to complete.
Having it in bite sized chunks really helped me to get started on the coding side of things.

![Flowchart for my Python Project](https://garys007.github.io/Project-3/assets/images/mock.png)

## Credits

* I found inspiration for the hangman drawings [here](https://itsourcecode.com/free-projects/python-projects/hangman-game-in-python-with-source-code/)
    * I made changes to this to suit my game better and also fixed a lint issue with the arms and legs due to using backslash(\). 
* I used this website to generate a [list of words](https://www.randomlists.com/random-words).
* I watched a variety of Youtube videos to get inspiration on my approach to building the game. 
    * [Video 1](https://www.youtube.com/watch?v=cJJTnI22IF8&t=103s&ab_channel=KylieYing) / [Video 2](https://www.youtube.com/watch?v=pFvSb7cb_Us&ab_channel=ShaunHalverson) / [Video 3](https://www.youtube.com/watch?v=6G4n3oY5Svo&ab_channel=YujianTang)
* Big thank you to the slack crew for helping me and motivating me along the way.    