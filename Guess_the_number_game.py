# -*- coding: utf-8 -*-
# Interactive Guess the Number Game 

"""

    The computer will think of a random number from 1 to 10 as 
    secret number.
    Then ask you ( Player ) to guess the number and store as 
    guess number.

    Compare the guess number with the secret number.
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""


import random 
print ("----GUESS THE NUMBER GAME----")
computer_number = random.randint(1,11)

x = input('Guess the number between 1 to 10:')

if (x == computer_number):
    print('You win , Computer lost')
else:
    print('Computer wins, You lost')

