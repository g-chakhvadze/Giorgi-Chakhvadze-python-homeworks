import random
list1 = [random.randint(1, 100) for _ in range(10)] 
list2 = [random.randint(1, 100) for _ in range(10)] 
list3 = [random.randint(1, 100) for _ in range(10)]
print("List 1:", list1) 
print("List 2:", list2) 
print("List 3:", list3)
for i in range(len(list1)): 
    sum_at_index = list1[i] + list2[i] + list3[i] 
    print(f"Sum at index {i}: {sum_at_index}")