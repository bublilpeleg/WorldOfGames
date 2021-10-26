import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    user_guess = int(input(f"Please enter a number between 1 to {difficulty}: "))
    return user_guess


def compare_results(secret_number, user_guess):
    if secret_number == user_guess:
        return True
    else:
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    won_or_lost = compare_results(secret_number, user_guess)
    if won_or_lost:
        print("you are WON in the GUESS GAME !")
        return 1
    else:
        print("You are LOST in the GUESS GAME !")
        return 0






