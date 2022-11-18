import random

totaalchips = 10
winchips = 35
totaalchips = (totaalchips + winchips)
print("je hebt", totaalchips, "chips totaal!")
print("-=-=-=-=-=-=-=-=-=-=-")

rollguess = random.randint(1,5)

roll = int(input('Place your bet, 1-5: '))
print('-=-=-=-=-=-=-=-=-=-=-')
if roll == rollguess:
        totaalchips = (totaalchips + winchips)
        print("je hebt", totaalchips, "chips totaal!")
        print(rollguess)
else:
        print('You lost')
        totaalchips = (totaalchips - totaalchips)
        print("je hebt", totaalchips, "chips totaal!")
        print(rollguess)