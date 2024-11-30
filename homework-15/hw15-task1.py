import random
random_numbers = [random.randint(1, 100) for _ in range(100)]
count_even = sum(1 for num in random_numbers if num % 2 == 0)
count_odd = 100 - count_even
number_counts = {
    "even": count_even,
    "odd": count_odd
}

print("Generated numbers:", random_numbers)
print("Number counts:", number_counts)
