#game
#check if user enter a number if not try again next time
#check if the user enter same random number
#how many attempts he take to enter corret number

start_number = input("enter a number to start the game: ")
if start_number.isdigit():
    start_number = int(start_number)
    if start_number <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("\nPlease enter the number next time")
    quit()

import random
random_number = random.randint(0,start_number)
no_of_guess = 0
while True:
    no_of_guess += 1
    guess_number = input("Guess the number: ")
    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("please type a Number")
        continue

    if guess_number == random_number:
        print("You got it in", no_of_guess, "guesses" )
        print("\nThanks for playing my mini work")
        break
    elif guess_number >= random_number:
        print("entered number is above")
    else:
        print("entered number is below")