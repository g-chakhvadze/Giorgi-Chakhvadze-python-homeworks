words = ["python", "code", "boy", "cat", "shawarma", "water", "life", "dog"]
filtered_words = [word for word in words if len(word) <= 3]
for word in filtered_words: 
    print(word.upper())