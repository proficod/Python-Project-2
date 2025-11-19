import random
import time

# How many digits should the secret number have
DIGITS = 4  # change this to 5, 6, etc.

# ------------------------------
# GLOBAL STATS
# ------------------------------
win_count = 0
times = []

# ------------------------------
# defs
# ------------------------------

# Random secret number
def make_secret():
    secret = ""
    digits = "0123456789"
    while len(secret) < DIGITS:
        d = random.choice(digits)
        if len(secret) == 0 and d == "0":
            continue
        if d not in secret:
            secret += d
    return secret

# Check if all rules are followed
def check_input(guess):
    if len(guess) != DIGITS:
        print(f"Enter exactly {DIGITS} digits\n")
        return False
    if not guess.isdigit():
        print("Enter only numbers.\n")
        return False
    if len(set(guess)) != DIGITS:
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

    for i in range(DIGITS):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    return bulls, cows

# One game
def play_game():
    global win_count, times

    print(f'''Hi there!
-----------------------------------------------
I've generated a random {DIGITS}-digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number
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

        print("Bulls:", bulls, "| Cows:", cows, "\n")

        if bulls == DIGITS:
            end_time = time.time()
            total = end_time - start_time
            minutes = int(total // 60)
            seconds = int(total % 60)

            # update statistics
            win_count += 1
            times.append(total)

            # calculate average time
            avg = sum(times) / len(times)
            avg_min = int(avg // 60)
            avg_sec = int(avg % 60)

            print("-----------------------------------------------")
            print("Congrats, you found out the number:", secret)
            print("Attempts:", attempts)
            print(f"Total time: {minutes:02d}:{seconds:02d}")
            print("-----------------------------------------------")

            print("Game statistics:")
            print("Total wins:", win_count)
            print(f"Average time: {avg_min:02d}:{avg_sec:02d}")
            print("-----------------------------------------------")

            break

# ------------------------------
# Repeat Game Cycle
# ------------------------------

while True:
    play_game()
    again = input("Wanna play again? (y/n): ").lower()
    if again != "y":
        print("\nThanks for playing! Byyyyyee!")
        break