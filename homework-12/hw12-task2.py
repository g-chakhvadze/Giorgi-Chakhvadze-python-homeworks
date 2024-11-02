import random
def num_generator():
    nums = []
    for i in range(50):
        random_num = random.randint(0,30)
        nums.append(random_num)
    return nums
def final_list(nums):
    expanded_list = []
    for num in nums:
        expanded_list.extend([num] * num)
    return expanded_list
if __name__=="__main__":
    generated_nums = num_generator()
    final_nums = final_list(generated_nums)
    print('Original list-',generated_nums)
    print('List-',final_nums)
    print('length-',len(final_nums))
