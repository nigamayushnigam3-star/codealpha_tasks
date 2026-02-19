import random

def hangman_game():
    # Predefined list of 5 words
    words = ["python", "computer", "programming", "internship", "challenge"]
    
    # Select random word
    word = random.choice(words).lower()
    word_letters = set(word)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6
    
    print("Welcome to Hangman Game!")
    print(f"Guess the word! You have {max_wrong} wrong guesses allowed.")
    
    while wrong_guesses < max_wrong and word_letters:
        # Display current progress 
        display = [letter if letter in guessed_letters else '_' for letter in word]
        print(f"\nWord: {' '.join(display)}")
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        # Get player input
        guess = input("Enter a letter: ").lower()
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        # Add to guessed letters
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word_letters:
            word_letters.remove(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry! '{guess}' is not in the word.")
    
    # Game end
    if word_letters:
        print(f"\nGame Over! The word was: {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word}")

# Run the game
if __name__ == "__main__":
    hangman_game()