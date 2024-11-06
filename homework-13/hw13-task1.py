import random
random_numbers = [random.randint(10,1000000000) for _ in range(100)]
shortest_number = min(random_numbers, key=lambda x: len(str(x)))
longest_number = max(random_numbers, key=lambda x: len(str(x)))
sorted_ascending = sorted(random_numbers, key=lambda x: len(str(x)))
sorted_descending = sorted(random_numbers, key=lambda x: len(str(x))), reverse=True

print("Shortest number:", shortest_number) 
print("Longest number:", longest_number) 
print("Sorted by length (ascending):", sorted_ascending) 
print("Sorted by length (descending):", sorted_descending)