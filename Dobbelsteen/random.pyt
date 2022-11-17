import random

def randnums():
   numbers = [] 
   for count in range(6):
        number = random.randint(1,9)
        numbers.append(number)
        print(number)
   print(sum(numbers))
randnums()