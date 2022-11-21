

def play_game():
    if int(input("Guess a number:"))!= 5:
          print("You Lose!")
    else:
          print("You Win!")

def play_again():
    return input("Play Again?").lower() == "y"

while True:
    play_game()
    if not play_again(): break

print ("OK Goodbye...")