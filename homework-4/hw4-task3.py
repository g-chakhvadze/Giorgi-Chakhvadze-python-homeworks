import random
n_positive_int = int(input("choose random positive integer from 0 to 1000: "))
if 0 < n_positive_int <1000:
   all_divisors = ""
   
   for divisors in range(1,n_positive_int+1):
        if n_positive_int % divisors == 0:
           all_divisors += str(divisors) + " "
           
   print(f"all divisors of {n_positive_int} are {all_divisors}.")
else:
    print("please enter right number.<3")
