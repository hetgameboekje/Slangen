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

def opnieuw():
    opnieuw = input("Wil je nog een keer gooien? (ja/nee) ")
    if opnieuw == "ja":
        getal()
        opnieuw()
    elif opnieuw == "nee":
        print("Bedankt voor het spelen!")
    else:
        print("Ongeldige invoer")
        opnieuw()