import random

totaalchips = 10
winchips = 35
inzet = 1


print("je hebt", totaalchips, "chips totaal!")
print("Je kan 35 chips winnen, Totaal is dit", totaalchips + winchips, "chips")
print("-=-=-=-=-=-=-=-=-=-=-")

for i in range(totaalchips):
        rollguess = random.randint(1, 2)

        roll = int(input('Place your bet, 1-36: '))
        print('-=-=-=-=-=-=-=-=-=-=-')
        if roll == rollguess:
                totaalchips = (totaalchips + winchips)
                print("Gefeliciteerd! je succesvol geraden, je hebt", totaalchips, "chips totaal!")

        else:
                print("Spel rolde:", rollguess)
                totaalchips = (totaalchips - inzet)
                print("je hebt verloren, je hebt", totaalchips, "chips totaal! ")
                
