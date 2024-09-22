n_positive_int = int(input("choose random positive integer from 0 to 20: "))
if 0 <= n_positive_int < 20:
    if n_positive_int == 0:
        print(0)
    elif n_positive_int == 1:
        print(1)
    else:
        a,b = 0,1
        b = 1
        for number in range(2,n_positive_int + 1):
          a,b = b, a + b
        print(b)
else:
    print("enter correct number.<3")