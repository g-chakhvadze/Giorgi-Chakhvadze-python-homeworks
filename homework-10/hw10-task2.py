def find_maximum(*numbers):
    if not numbers:  
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(find_maximum(10, 20, 5, 8, 30))         
print(find_maximum(-1, -5, -10, -3))           
print(find_maximum(10, 500, 200, 400, 300))