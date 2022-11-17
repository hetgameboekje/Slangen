# Importeren van de random module
import random
# Functie om een willekeurig getal te genereren
def getal():
#vraag gebruiker om aantal dobbelstenen
    aantal = int(input("Hoeveel dobbelstenen wil je gooien? "))
    for i in range(aantal):
        print(random.randint(1,6))


getal()
#functie om gebruiker te vragen of ze het opnieuw willen doen


import random

def rollen(min, max):
    while True:
        print(f"Jouw dobbelsteen is {random.randint(min, max)}")
        answer = input("Wil je nog een keer rollen? (y/n) ")
        if answer == "n":
            break

rollen(1, 6)
   