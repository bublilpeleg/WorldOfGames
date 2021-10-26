from MemoryGame import play as play_memory_game
from GuessGame import play as play_guess_game
from CurrencyRouletteGame import play as play_roullette_game
from Score import add_score
from MainScores import hello


def welcome():
    name = input("Please enter your name: ")
    return name, print(f"Hello {name} and welcome to the World of Games(WoG).\nHere you can find many cool games play.")


def load_game():
    print("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you "
          "have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency "
          "Roulette - try and guess the value of a random amount of USD in ILS")

    game_chosen = None
    while game_chosen is None:
        game_chosen = int(input("Please enter the game do you want to play :"))
        if game_chosen < 1 or game_chosen > 3:
            game_chosen = None
            print("You must enter number between 1-3")

    game_difficulty = int(input("Please choose game difficulty from 1 to 5: "))
    while game_difficulty > 5 or game_difficulty == 0:
        game_difficulty = int(input("You Must enter number between 1-3.\nPlease choose game difficulty from 1 to 5: "))

    if game_chosen == 1:
        result = play_memory_game(game_difficulty)
        if result == 1:
            add_score(game_difficulty)
    elif game_chosen == 2:
        result = play_guess_game(game_difficulty)
        if result == 1:
            add_score(game_difficulty)
    elif game_chosen == 3:
        result = play_roullette_game(game_difficulty)
        if result == 1:
            add_score(game_difficulty)
