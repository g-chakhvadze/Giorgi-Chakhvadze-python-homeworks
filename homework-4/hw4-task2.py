import random
n_positive_int = int(input("choose random positive integer from 0 to 30: "))
max_value = 0
if 0 < n_positive_int < 30:
    print("generated numbers are: ")
    for numbers in range(n_positive_int):
        numbers = random.randint(0,1000)
        print(numbers)
        if numbers > max_value:
            max_value = numbers 
    print(f"max number is {max_value}")
else:
    print("please write the correct number")
