"""
In this game, the user puts in a number and the program comes up with a 
random number that's less than the user's inputted number. 
Then the user guesses the number.
The program gives hints to the user to state if the number they guessed it
below or above the actual number until the user guesses it
Finally, the program tells the user how many guesses the user had to 
get the correct number
"""
import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    # String digit needs to be converted to a integer
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print ("Please type a number larger than 0 next time.")
        quit()
else:
    print ("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
# To count how many times the user has correct guesses
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
    # String digit needs to be converted to a integer
        user_guess = int(user_guess)
    else:
        print ("Please type a number next time.")
        continue

    if user_guess == random_number:
        print ("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")
# same as 
# print("You got it in " + str(guesses) + " guesses")


    
