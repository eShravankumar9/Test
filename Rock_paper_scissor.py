import random
computer_choice = random.choice(['scissors','rock','paper'])

user_choice = input('Do you want - rock, paper, or scissors? \n')
if computer_choice == user_choice:
    print("The computer choice is"+" " + computer_choice)
    print("TIE")
elif user_choice == 'rock' and computer_choice == 'scissors':
     print("The computer choice is"+" " + computer_choice)
     print("Win")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("The computer choice is"+" " + computer_choice)
    print("Win")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("The computer choice is"+" " + computer_choice)
    print("Win")
else:
    print("you lose :( computer wins :D")
    print("The computer choice is"+" " + computer_choice)

