n = int(input("write a number 0<=n<=10000: "))
if 0 <= n <= 10000:

    reversed_num = 0
    digit_sum = 0
    temp = n
    while temp >0:
        digit = temp % 10
        reversed_num = reversed_num *10 + digit
        digit_sum += digit
        temp //= 10 #ბოლო ციფრს აშორებს რიცხვს ათზე გაყოფის შემდეგ
    print(reversed_num)
    print(digit_sum)
else:
    print("write correct number.")
    