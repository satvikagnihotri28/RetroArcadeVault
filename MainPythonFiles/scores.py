from storage import y, q
from helpers import t, w
listscores = q("scores.txt")
def a():
    """Records a new high score."""
    print("\n^^ SUBMIT HIGH SCORE ^^")
    player = t("Enter player name: ")
    game = t("Enter game name : ")
    score = w("Enter score: ")
    entry = player+" - "+game+"-"+str(score)
    listscores.append(entry)
    y("scores.txt", listscores)
    print("Your Score has been saved successfully.")
def b():
    """Displays all recorded high scores."""
    print("\n^^^^ HIGH SCORE VAULT ^^^^")
    if len(listscores)==0:
        print("No scores have been registered yet.")
    else:
        for item in listscores:
            print(item)

'''
Welcome to the score tracking zone! This file manages all the high scores 
tied to specific players and classic arcade games. It handles collecting score 
data, organizing records, and getting them ready to be saved or displayed.
'''