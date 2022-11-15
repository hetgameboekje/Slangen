import random

def rollen(min, max):
    while True:
        print(f"Jouw dobbelsteen is {random.randint(min, max)}")
        answer = input("Wil je nog een keer rollen? (y/n) ")
        if answer == "n":
            break

rollen(1, 6)
   