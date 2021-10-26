import random
import time


def generate_sequence(difficulty):
    my_list = [random.randrange(1, 101) for i in range(difficulty)]
    print(my_list, end='')
    time.sleep(1)
    print(20 * '\b' + " ")
    return my_list


def get_list_from_user(difficulty):
    user_list = []
    guess = difficulty
    print(f"Enter the {difficulty} numbers that do you remember:\n(Press Enter After every guess)\n ")
    for x in range(difficulty):
        user_list.append(int(input()))
        print(f"You have {guess - 1} more guesses left: ")
        guess = guess - 1
    return user_list


def is_list_equal(my_list, user_list):
    if my_list == user_list:
        return True
    else:
        return False


def play(difficulty):
    my_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    won_or_lost = is_list_equal(my_list, user_list)
    if won_or_lost:
        print("you are WON in the GUESS GAME !")
        return 1
    else:
        print("You are LOST in the GUESS GAME !")
        return 0



