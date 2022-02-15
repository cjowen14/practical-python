import random

def guessing():
    global number_of_guesses
    number_of_guesses += 1

    guess = int(input("Your guess?"))
    
    if guess == the_number:
        print("Great job", name, "you found my number in", number_of_guesses, "tries!")
    elif guess > the_number:
        print("Your guess is too high. Try again.")
        guessing()
    else:
        print("Your guess is too low. Try again.")
        guessing()

the_number = random.randint(1,100)

number_of_guesses = 0

name = input("Hello there, what's your name?\n")
print(name, "I'm thinking of a number between 1 and 100")
print("Try to guess the number.")

guessing()