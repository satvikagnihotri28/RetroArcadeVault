from storage import y, q
from helpers import t
d = q("players.txt")
def x():
    print("\n^^^ REGISTER NEW PLAYER ^^^")
    name = t("Enter player name : ")
    if name in d:
        print("Player already exists in the system!!!")
    else:
        d.append(name)
        y("players.txt", d)
        print("Player "+name+" added successfully..")
def z():
    print("\n^^^ REGISTERED PLAYERS ^^^")
    if len(d)==0:
        print("No players found....")
    else:
        for index in range(len(d)):
            print(str(index + 1)+"."+d[index])

'''
This module handles everything related to our arcade players. 
It lets you sign up new players with unique handles and makes sure nobody 
takes an already registered name. You can also pull up a clean list of 
everyone currently hanging out in the vault.
'''