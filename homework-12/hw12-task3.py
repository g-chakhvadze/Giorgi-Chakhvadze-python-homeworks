import random
def num_generator():
    nums = []
    for i in range(50):
        nums.append(random.randint(1,30))
    return nums

def modified_nums(nums):
    unique_nums = list(set(nums))
    return unique_nums

if __name__=="__main__":
    original_nums = num_generator()
    final_nums = modified_nums(original_nums)
    print("Generated list is-",original_nums)
    print("Final list is-",final_nums)
    print("Length of final list is-",len(final_nums))
    
