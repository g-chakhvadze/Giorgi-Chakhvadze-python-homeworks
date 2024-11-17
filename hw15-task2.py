def count_characters(input_string):
    character_counts = {}
    for char in input_string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    for char, count in character_counts.items():
        print(f"{char} – {count}")

input_string = input("write string: ")
count_characters(input_string)
