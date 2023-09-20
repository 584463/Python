from random import choice

# List of words to choose from
words = [
  "python",
  "hangman",
  "programming",
  "computer",
  "gaming",
  "javascript",
  "money",
  "game",
  "hitler",
  "happy",
  "tv",
  "iphone",
  "sadnesm",
  "java",
  "cat",
  "comma",
  "911"]


# Choose a random word from the list
word = choice(words)


# Create a list to store the guessed letters
guessed_letters = []


# Set the number of allowed incorrect guesses
max_attempts = 6
incorrect_guesses = 0


# Create a list to store the correctly guessed letters and placeholders
word_progress = ["_"] * len(word)


# Main game loop
while True:
    # Display current progress
    print(" ".join(word_progress))
    
    # Get a guess from the player
    guess = input("Guess a letter: ").lower()
    
    # Check if the guess is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    # Add the guessed letter to the list
    guessed_letters.append(guess)
    
    # Check if the guess is in the word
    if guess in word:
        # Update word progress
        for i in range(len(word)):
            if word[i] == guess:
                word_progress[i] = guess
        # Check if the player has won
        if "_" not in word_progress:
            print("Congratulations! You guessed the word:", word)
            break
    else:
        print("Incorrect guess!")
        incorrect_guesses += 1
        print("Attempts remaining:", max_attempts - incorrect_guesses)
        
        # Check if the player has run out of attempts
        if incorrect_guesses == max_attempts:
            print("You ran out of attempts. The word was:", word)
            break