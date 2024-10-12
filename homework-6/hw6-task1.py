import random
prog_num=random.randint(0,99)
count=0
print(prog_num)
while count<11:
    user_num = int(input("write your number from 1 to 100: "))
    if prog_num == user_num:
        print("you are the winner!")
        break
    elif prog_num < user_num:
        print("your number is higher than my number")
    elif prog_num > user_num:
        print("your number is lower than my number")
    else:
        print("write correct number!")
    count+=1
else:
    print("computer won.")
