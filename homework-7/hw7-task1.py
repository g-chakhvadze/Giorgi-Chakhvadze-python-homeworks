word = input("write a random word: ")
for i in range(0,len(word)):
    if i % 2 !=0:
         if word[i] != "e":
             print(word[i])
