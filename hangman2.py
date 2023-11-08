picture0 = """
    ___________
    |        
    |      
    |        
____|_____________
"""
picture1 = """
    ___________
    |         O
    |      
    |        
____|_____________
"""
picture2 = """
    ___________
    |         O
    |         |
    |        
____|_____________
"""
picture3 = """
    ___________
    |         O
    |         |--
    |        
____|_____________
"""
picture4 = """
    ___________
    |         O
    |       --|--
    |        
____|_____________
"""
picture5 = """
    ___________
    |         O
    |       --|--
    |        /
____|_____________
"""
picture6 = """
    ___________
    |         O
    |       --|--
    |        / \\
____|_____________
"""
pictures = [picture0, picture1, picture2, picture3, picture4, picture5, picture6]




wrong_guess = 0
secret_word = "Parmesan"
secret_word = secret_word.upper()

def setup_word(secret_word):
    known_letter = []
    for i in range(len(secret_word)):
        known_letter.append("_")

    return known_letter


def draw_board(wrong_guesess, known_letters):
    print(pictures[wrong_guesess])
    for lettter in known_letters:
        print(lettter, end=" ")


known_letters = setup_word(secret_word)


playing = True
while playing:
    draw_board(wrong_guess, known_letters)
    guess = input("Guess a letter: ")
    while len(guess) !=1:
        print("Invaild")
        guess = input("\nGuess a letter: ")




    if guess.upper() in secret_word:
        print(f"{guess} was in the word")

        for i in range(len(secret_word)):
            if guess.upper() == secret_word[i]:
                known_letters[i] = guess.upper()


    else:
        print("worng")
        wrong_guess += 1
        if wrong_guess == 6:    
            playing = False




print("Game Over")