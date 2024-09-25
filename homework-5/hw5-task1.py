n = int(input("შეიყვანეთ რიცხვი 0-დან 50-მდე: "))
if 0 < n < 50:
    i = 1 #ვიწყებთ ათვლას n-მდე
    while i <= n :
        print(f"{i} - ", end =" ")
        j = 1 #ვამოწმებთ გამყოფებს
        printed = 0
        while j <= i:
            if i % j == 0:
                if printed < 3:
                    print(j, end=" ")
                    printed += 1
            j += 1
        print()
        i += 1
    else:
        print("შეიყვანეთ შესაბამისი რიცხვი.")