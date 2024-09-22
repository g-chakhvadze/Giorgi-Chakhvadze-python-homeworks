import random
players_number = int(input("Enter players number: "))
for player in range(players_number):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(dice1, dice2)