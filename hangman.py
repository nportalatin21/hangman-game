from random import choice

word = choice(['Algorithm',
        'Encryption',
        'Database',
        'Firewall',
        'API',
        'Server',
        'Protocol',
        'HTML',
        'CSS',
        'JavaScript',
        'Compiler',
        'Debugging',
        'Virtualization',
        'Artificial Intelligence',
        'Machine Learning',
        "Cloud Computing",
        "Big Data",
        "Cybersecurity",
        "Network",
        "Operating System"]).lower()

print(word)




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

def display_word(word, guessed_letters): # defines a function called display_word
    display = "" # empty string called display
    for letter in word: #Iterates over each letter in the word parameter.
        if letter in guessed_letters: #Checks if the letter is in the guessed_letters list.
            display += letter # it appends the letter to the display string.
        else: # Executes if the letter is not in guessed_letters.
            display += "_" # Appends an underscore (_) to the display string.
    print("Current word:", display) # Prints the current state of the word, with guessed letters revealed and underscores for unguessed letters.
    return display # Returns the display string.

def game_board(guess, attempts): # Taking in two parameters named guess and attempts. 
    if guess in word: 
        print("Good guess")
        guessed_letters.append(guess)
        # print(HANGMAN_PICS[attempts])

    else:
        print("Oops! That is not correct.")
        print(HANGMAN_PICS[attempts]) 
    attempts += 1  # Increment the number of attempts
        
    
    display = display_word(word, guessed_letters)

    if "_" not in display:  # Check if the word is fully guessed
        print("Winner!")  # The player has guessed the entire word
        return
    elif attempts < 7:  # Check if the player has more attempts left
        another_guess = input("Guess again: ")
        game_board(another_guess, attempts)
    else:
        print("Game over")  # The player has reached the maximum number of attempts
        return # ends the function 
guess = input("Guess the letter: ")
game_board(guess, 0)  # Start the game with 0 attempts
