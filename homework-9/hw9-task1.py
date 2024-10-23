n = int(input("random num n>1: "))
i = 1
answer = 0
if n>1:
    while i<n:
        formula = ((-1)**i)/(2*(i+1)-1)
        answer = answer + 4 * formula
        i+=1
    x = answer + 4
    print(x,answer,formula) 
