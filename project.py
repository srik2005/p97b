import random

chances = 1 
number=random.randint(1,10)
guess = int(input("Enter Your Guess:"))

while (guess != number and chances<5):
    if (guess < number):
        print("Your Guess is Higher. Try again") 
        guess=int(input("Enter Your Guess:"))
        chances= chances + 1
    else:
        print("Your Guess is Lower. Try Again")   
        guess=int(input("Enter Your Guess:")) 
        chances= chances + 1




if (guess==number):
    print("You Win!!!!!!!")

if not chances<5:
    print("You Lose!!!!!!!")   