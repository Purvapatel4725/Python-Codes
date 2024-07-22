#Purva Patel #100886734
import random

def bot(comp,player):
    if comp == "r":
        if player == "p":
            print("\tPlayer wins.")
        elif player == "s":
            print("\tcomp wins.")
        elif player == "p":
            print("\tTie.")
    elif comp == "p":
        if player == "r":
            print("\tcomputer wins.")
        elif player == "s":
            print("\tplayer wins.")
        elif player == "p":
            print("\tTie.")
    elif comp == "s":
        if player == "r":
            print("\tPlayer wins.")
        elif player == "p":
            print("\tcomp wins.")
        elif player == "p":
            print("\tTie.")


a = True
while a == True:
    comp = random.randint(0,2)
    if comp == 0:
        comp = "r"
    elif comp == 1:
        comp = "p"
    elif comp == 2:
        comp = "s"
    player = input("enter any thing you want to choose: ")
    if player == "exit":
        print("you exited the game.")
        break
    else:
        print(f"\tcomp choose: {comp}")
        print(f"\tyou choose: {player}")
        bot(comp,player)



