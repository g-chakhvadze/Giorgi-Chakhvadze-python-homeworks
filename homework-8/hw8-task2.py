first_string = input("Input first string: ")
second_string = input("Input second string: ")

for char in second_string:
    if char != " ": 
        if second_string.count(char) > first_string.count(char):
            print("Output: NO")
            break
else:
    print("Output: YES")
    