word = input("write random word: ")
if len(word)<2:
    print("a word must contain at least 2 symbols: ")
else:
    first_letter = word[0]
    last_letter = word[-1]
    if len(word) % 2 ==0:
        mid_letter1 = word[int(len(word)/2 - 1)]
        mid_letter2 = word[int(len(word)/2)]
        mid_letters = mid_letter1 + " " + mid_letter2
    else:
        mid_letters = word[int(len(word)/2)]
    count = 0
    while count <5:
        print(f"first letter is {first_letter}, middle letter is/are {mid_letters}, last letter is {last_letter}.")
        count+=1