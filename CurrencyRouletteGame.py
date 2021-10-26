import requests
import random


def get_money_interval(difficulty):
    random_number = random.randint(1, 100)
    print(f"what he thinks is the value of the {random_number} from USD to ILS")
    url = 'http://api.exchangeratesapi.io/v1/latest?access_key=859dc9f4da7cc6f8f1717aaecaae001c&symbols=USD,ILS'
    response = requests.get(url)
    data = response.json()
    USD = (data['rates']['USD'])
    ILS = (data['rates']['ILS'])
    convert = ILS / USD
    return [random_number * convert, random_number * convert - (5 - difficulty),
            random_number * convert + (5 - difficulty)]


def get_guess_from_user():
    user_guess = float(input("Enter your guess :"))
    return user_guess


def play(difficulty):
    range = get_money_interval(difficulty)
    user_guess = get_guess_from_user()
    if range[1] < user_guess < range[2]:
        print(True)
        return 1
    else:
        print(False)
        return 2


