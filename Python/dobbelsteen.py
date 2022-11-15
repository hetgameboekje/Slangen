# Importeren van de random module
import random
# Functie om een willekeurig getal te genereren
def getal():
#vraag gebruiker om aantal dobbelstenen
    aantal = int(input("Hoeveel dobbelstenen wil je gooien? "))
    for i in range(aantal):
        print(random.randint(1,6))

#geef gebruiker het aantal ogen van de dobbelstenen
getal()
#vraag gebruiker of hij nog een keer wil gooien

#als gebruiker ja zegt, doe het nog een keer
#als gebruiker nee zegt, stop
