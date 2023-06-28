word = "ant"
guessed_letters = [] # empty list tracking correct letters

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
    ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
    ===''']

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print("Current word:", display)

def game_board(guess, attempts):
    if guess in word:
        print("Good guess")
        guessed_letters.append(guess)
        print(HANGMAN_PICS[attempts])
    else:
        print("Oops! That is not correct.")
        print(HANGMAN_PICS[attempts])

    attempts += 1  # Increment the number of attempts
    display_word(word, guessed_letters)

    if "_" not in display_word(word, guessed_letters):  # Check if the word is fully guessed
        print("Winner!")  # The player has guessed the entire word
    elif attempts < 7:  # Check if the player has more attempts left
        another_guess = input("Guess again: ")
        game_board(another_guess, attempts)
    else:
        print("Game over")  # The player has reached the maximum number of attempts

guess = input("Guess the letter: ")
game_board(guess, 0)  # Start the game with 0 attempts
