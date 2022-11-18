import random

totaalchips = 10
winchips = 35

print("je hebt", totaalchips, "chips totaal!")
print ("Je kan 35 chips winnen, Totaal is dit", totaalchips+ winchips,"chips")
print("-=-=-=-=-=-=-=-=-=-=-")

rollguess = random.randint(1,5)

roll = int(input('Place your bet, 1-5: '))
print('-=-=-=-=-=-=-=-=-=-=-')
if roll == rollguess:
        totaalchips = (totaalchips + winchips)
        print("Gefeliciteerd! je succesvol geraden, je hebt", totaalchips, "chips totaal!")
        
else:
        print("Spel rolde:", rollguess)
        totaalchips = (totaalchips - totaalchips)
        print("je hebt verloren, je hebt", totaalchips, "chips totaal! ")