#This game will have the user guess a nuber between 1 and 100

import random
chance = 6
num =random.randint(1, 100)

print("Welcome to Higher or Lower!")
print("I am thinking of a number between 1 and 100.")


for i in range(6):
    guess = int(input("Waht you thinking of nunber is?"))

    if guess == num:
        print("You win boy!")
        break


    if guess > num:
        print("Incorrect. Your guess is to high boy.")
        chance = chance - 1
        guess = int(input("ask again "))

    if guess < num:
        print("Incorrect. Your guess is to low boy.")
        chance = chance - 1
        guess = int(input("ask again "))

        if chance == 0:
            break



print("Game over boy.")

if chance == 0 and guess != num:
    print(f"You lose boy. The answer Was {num}")
