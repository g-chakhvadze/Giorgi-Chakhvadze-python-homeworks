import random
import math
counter = 0
n = int(input("random number n>1: "))
if n >1:
    for i in range(n):
        a = random.uniform(0,1)
        b = random.uniform(0,1)
        if math.sqrt(a**2+b**2)<=1:
            counter+=1
    result = 4*counter/n
    print(f"result: {result}")
