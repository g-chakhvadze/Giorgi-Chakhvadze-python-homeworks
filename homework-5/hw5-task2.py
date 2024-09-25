i = 1
while i <= 9:
    j = 1
    while j <= i:
        multiplication = i * j
        print(f"{j} * {i} = {multiplication}", end=" ")
        j += 1
    print()
    i += 1