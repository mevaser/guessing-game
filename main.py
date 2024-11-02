import art
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess_num, chosen_num, attempts):
    """Checks answer against guess, returns the number of turns remaining."""
    if guess_num > chosen_num:
        print("Too high.")
        return attempts - 1
    elif guess_num < chosen_num:
        print("Too low.")
        return attempts - 1
    else:
        print(f"Well done. The answer is {chosen_num} 😎")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print(art.logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 to 100.")
    chosen_number = random.randint(1,100)
    attempts_left = set_difficulty()
    guess = 0

    while guess != chosen_number:
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts_left = check_answer(guess, chosen_number,attempts_left)
        if attempts_left == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != chosen_number:
            print("Guess again.")

game()