from storage import y, q, t
d = q("players.txt")
def x():
    """Register a new player profile if the username is unique."""
    print("\n^^^ REGISTER NEW PLAYER ^^^")
    name = t("Enter player name : ")
    if name in d:
        print("Player already exists in the system!!!")
    else:
        d.append(name)
        y("players.txt", d)
        print("Player "+name+" added successfully..")

def z():
    """Display a numbered list of all registered players."""
    print("\n^^^ REGISTERED PLAYERS ^^^")
    if len(d)==0:
        print("No players found....")
    else:
        for index in range(len(d)):
            print(str(index + 1)+"." + d[index])