import random

totaalDobbel = []

aantal = int(input("Hoeveel dobbelstenen wil je gooien? "))
for i in range(aantal):
        print(random.randint(1,6))