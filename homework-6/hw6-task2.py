n = int(input("write any positive number 0<n<=1000: "))
if 0 < n <= 1000:
    while n != 1:
        print(f"{n}->",end="")
        if n % 2 ==0:
            n = n/2
        else:
            n = n*3 + 1
    print(1.0)
else:
    print("write correct number.")