def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


print(count_vowels("hello"))  
print(count_vowels("hello world"))  
print(count_vowels("Python"))