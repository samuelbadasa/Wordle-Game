import random

WORD_LIST = [
    "HEART",
    "DOORS",
    "REACH",
    "BEACH",
    "FETCH",
]

def print_color(char, color):
    if color == "GREEN":
        print('\33[32m', end="")
    elif color == "YELLOW":
        print('\33[33m', end="")
    elif color != "BLACK":
        print("Please choose 'GREEN', 'YELLOW', or 'BLACK'")
    print(char + '\033[0m', end=" ")
        

def select_random_word():
    return WORD_LIST[random.randrange(len(WORD_LIST))].lower()
