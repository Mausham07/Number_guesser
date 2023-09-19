# import random to use
import random

# Print the welcome 
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 50.")

level = input("Choose a difficulty. Type 'noob' or 'pro': ").lower()

computer_number = random.randint(1, 51)

if level == 'noob':
    num_of_chance = 8
    flag = False
    while flag == False:
        guess = int(input("Make a guess: "))

        if computer_number == guess:
            print("You guessed the correct number.")
            flag = True
        elif computer_number > guess:
            print(f"You guessed low. Now you have {num_of_chance} tries left.")
        
        else:
            print(f"You guessed high. Now you have {num_of_chance} tries left.")
        
        num_of_chance = num_of_chance - 1

        if num_of_chance == 0:
            print(f"Sorry you could not guess the correct number. The correct number is {computer_number}.")
            flag = True