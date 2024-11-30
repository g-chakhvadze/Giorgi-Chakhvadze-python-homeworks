n=int(input("შეიყვანეთ რიცხვი 10<=n<=5432: "))
if n<10 or n>5432:
    print("პროგრამას გადმოეცა არასწორი რიცხვი")
elif n>=10 and n<13:
    print("არც ერთი რიცხვია 13-ის ჯერადი")
else:
    nums=[]
    count=0
    for i in range(13,n+1):
        if i%13==0:
            nums.append(i)
            count+=1
    print(f"ცამეტის ჯერადი რიცხვებია:",nums)
    print(f"მათი რაოდენობაა {count}")

