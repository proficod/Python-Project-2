import random
import time

# defs
# Random secret number
def make_secret():
    secret = ""
    digits = "0123456789"
    while len(secret) < 4:
        d = random.choice(digits)
        if len(secret) == 0 and d == "0":
            continue
        if d not in secret:
            secret += d
    return secret

# Check if all rules are followed
def check_input(guess):
    if len(guess) != 4:
        print("Enter exactly 4 digits\n")
        return False
    if not guess.isdigit():
        print("Enter only numbers.\n")
        return False
    if len(set(guess)) != 4:
        print("Each number should appear only once.\n")
        return False
    if guess[0] == "0":
        print("The number should not start from 0.\n")
        return False
    return True

# Count of bulls and cows
def get_bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    return bulls, cows

# Одна игра
def play_game():
    print('''Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------''')
    
    secret = make_secret()
    attempts = 0

    start_time = time.time()

    while True:
        guess = input("Your number: ")

        if not check_input(guess):
            continue

        attempts += 1
        bulls, cows = get_bulls_and_cows(secret, guess)

        print("Bulls", bulls, "| Cows:", cows, "\n")

        if bulls == 4:
            end_time = time.time()
            total = end_time - start_time
            print("Congrats, you found out the number:", secret)
            print("Attempts:", attempts)
            print("Total time:", round(total, 1), "seconds\n")
            break

# ------------------------------
# Repeat Game Cycle
# ------------------------------

while True:
    play_game()
    again = input("Wanna play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! Byyyyyee!")
        break