# modul pro práci s pseudo-náhodnými procesy    
import random
# modul pro praci se stopky
import time

welcome_text = ('''
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------''')
print(welcome_text)

def random_number():
    number = random.randint(1023, 9876)
    return number

number = random_number
print(number)

