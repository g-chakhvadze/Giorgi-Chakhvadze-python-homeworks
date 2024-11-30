import random
def win_or_lose(user_choice):
    comp_choice_list=["r","p","s"]
    comp_choice=random.choice(comp_choice_list)
    print(f"computer chose:{comp_choice}")
    if comp_choice==user_choice:
        print("it is a tie, try again")
        user_choice_again=input("try again, r,s or p? ")
        win_or_lose(user_choice_again)
    else:
        if user_choice=="r" and comp_choice=="s":
            print("you won.")
    
        elif user_choice=="r" and comp_choice=="p":
            print("you lose")
        elif user_choice=="s" and comp_choice=="p":
            print("you won")
        elif user_choice=="s" and comp_choice=="r":
            print("you lose")
        elif user_choice=="p" and comp_choice=="r":
            print("you won")
        else:
            print("you lose")



def main():
    user_choice=(input("R,P or S? "))
    win_or_lose(user_choice)
if __name__=="__main__":
    main()
