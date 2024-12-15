def add_friend(friends_dict, person1, person2):
    if person1 not in friends_dict:
        friends_dict[person1] = []
    if person2 not in friends_dict:
        friends_dict[person2] = []
    if person2 not in friends_dict[person1]:
        friends_dict[person1].append(person2)
    if person1 not in friends_dict[person2]:
        friends_dict[person2].append(person1)

def print_friends(friends_dict):
    for person in friends_dict:
        friends = ', '.join(friends_dict[person])
        print(f"{person} – {friends}")

def main():
    friends_dict = {}
    while True:
        user_input = input("write information (FINISH to end): ")
        if user_input == "FINISH":
            break
        try:
            person1, person2 = user_input.split(" – ")
            add_friend(friends_dict, person1, person2)
        except ValueError:
            print("invalid format,try again.")

    print_friends(friends_dict)

# პროგრამის გაშვება
main()
