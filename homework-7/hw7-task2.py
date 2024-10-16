word = input("write a random word: ")
for i in range(0,len(word)):
    if word[i] not in "aeiouAEIOU":
        print(word[i])