import wordlist

# Get a random word from the word list
def get_word():
    word = wordlist.get_random_word()
    return word.upper()

# Add spaces between letters
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces

# Draw the display
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("-" * 79)
    draw_hangman(num_wrong)
    print("Word:", add_spaces(displayed_word),
          "  Guesses:", num_guesses,
          "  Wrong:", num_wrong,
          "  Tried:", add_spaces(guessed_letters))

def draw_hangman(num_wrong):
    print("____")
    print("    |")
    if num_wrong == 0:
        print()
    if num_wrong == 1:
        print("    O\n")
    elif num_wrong == 2:
        print("    O")
        print("    |\n")
    elif num_wrong == 3:
        print("    O")
        print("   \\|\n")
    elif num_wrong == 4:
        print("    O")
        print("   \\|/\n")
    elif num_wrong == 5:
        print("    O")
        print("   \\|/")
        print("    |\n")      
    elif num_wrong == 6:
        print("    O")
        print("   \\|/")
        print("    |")      
        print("   /\n")
    elif num_wrong == 7:
        print("    O")
        print("   \\|/")
        print("    |")      
        print("   / \\\n")

# Get next letter from user
def get_letter(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().upper()
    
        # Make sure the user enters a letter and only one letter
        if guess == "" or len(guess) > 1:
            print("Invalid entry. ",
                  "Please enter one and only one letter.")
            continue
        # Don't let the user try the same letter more than once
        elif guess in guessed_letters:
            print("You already tried that letter.")
            continue
        else:
            return guess

# The input/process/draw technique is common in game programming
def play_game():
    word = get_word()
    
    word_length = len(word)
    remaining_letters = word_length
    displayed_word = "_" * word_length

    num_wrong = 0               
    num_guesses = 0
    guessed_letters = ""

    draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    while num_wrong < 7 and remaining_letters > 0:
        guess = get_letter(guessed_letters)
        guessed_letters += guess
        
        pos = word.find(guess, 0)
        if pos != -1:
            displayed_word = ""
            remaining_letters = word_length
            for char in word:
                if char in guessed_letters:
                    displayed_word += char
                    remaining_letters -= 1
                else:
                    displayed_word += "_"              
        else:
            num_wrong += 1

        num_guesses += 1

        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    print("-" * 79)
    if remaining_letters == 0:
        print(f"Congratulations! You got it in {num_guesses} guesses.")    
    else:    
        print("Sorry, you lost.")
        print(f"The word was: {word}")

def main():
    print("Play the H A N G M A N game")
    draw_hangman(7)

    again = "y"
    while again.lower() == "y":
        play_game()
        print()
        again = input("Do you want to play again (y/n)?: ")

    print("Bye!")

if __name__ == "__main__":
    main()
