from storage import y, q
from helpers import t, w

listscores = q("scores.txt")

def a():
    """Record and store a new high score entry linked to a player and game."""
    print("\n^^ SUBMIT HIGH SCORE ^^")
    player = t("Enter player name: ")
    game = t("Enter game name : ")
    score = w("Enter score: ")
    entry = player+" - "+game+"-"+str(score)
    listscores.append(entry)
    y("scores.txt", listscores)
    print("Your Score has been saved successfully.")

def b():
    """Display all recorded high scores from the vault."""
    print("\n^^^^ HIGH SCORE VAULT ^^^^")
    if len(listscores)==0:
        print("No scores have been registered yet.")
    else:
        for item in listscores:
            print(item)