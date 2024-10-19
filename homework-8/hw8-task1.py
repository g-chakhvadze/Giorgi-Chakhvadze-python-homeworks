word = input("random word: ")
new_word = ""

# სივრცეების მოცილება და შებრუნებული ტექსტის შექმნა
for i in range(len(word) - 1, -1, -1):  # უკანიდან წინ
    if word[i] != " ":  # სივრცეების უგულებელყოფა
        new_word += word[i]

# ქვედა რეგისტრში გადაყვანა
new_word = new_word.lower()
word_without_space = word.replace(" ", "").lower()  # სივრცეების გარეშე ტექსტი

# პალინდრომის შემოწმება
if new_word == word_without_space:
    print("input:", word)
    print("Is palindrome")
else: 
    print("input:", word)
    print("Is not palindrome")

# დაბეჭდე შებრუნებული ტექსტი და საწყისი ტექსტი
print("reversed text:", new_word)
print("original text:", word)