import random


def play_game():
    winchips = 35
    inzet = 1
    totaalchips = 10
    while totaalchips == 0:
        print("You have no more chips left!")
        play_again()

    print("je hebt", totaalchips, "chips totaal!")
    print("Je kan 35 chips winnen, Totaal is dit", totaalchips + winchips, "chips")
    print("-=-=-=-=-=-=-=-=-=-=-")

    for i in range(totaal_chips):
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
                

              
def play_again():
    if input("Do you want to play again? (y/n)") == "y":
        play_game()
        play_again()
    else:
        print("Thanks for playing!")
        exit()
    

while True:
    play_game()
    if not play_again(): break

print ("OK Goodbye...")