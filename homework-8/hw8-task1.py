word = input("random word: ")
new_word = ""

for i in range(len(word) - 1, -1, -1):  
    if word[i] != " ":  
        new_word += word[i]

new_word = new_word.lower()
word_without_space = word.replace(" ", "").lower()  

if new_word == word_without_space:
    print("input:", word)
    print("Is palindrome")
else: 
    print("input:", word)
    print("Is not palindrome")
    