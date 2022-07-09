import random

roll = random.randint(1,6)

guess= int(input("guess the dice roll\n"))
#print("The computer rolled a " +str(roll))

if guess== roll:
    print("you Win computer rolled a"+" "+ str(roll))
else:
    print("you lose computer rolled a"+" "+ str(roll))