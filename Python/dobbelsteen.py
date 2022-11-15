import random
min = 1
max = 6

raw_input = input("Roll the dices again?")
while roll_again == "yes" or roll_again == "y":
    print (random.randint(min, max))
    print (random.randint(min, max))
    roll_again = input("Roll the dices again?")