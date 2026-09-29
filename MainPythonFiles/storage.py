def y(nn, e):
    try:
        file = open(nn,"w")
        for item in e:
            file.write(item+"\n")
        file.close()
    except:
        print("Can not save to file...")

def q(nn):
    e=[]
    try:
        file=open(nn,"r")
        for line in file:
            e.append(line.strip())
        file.close()
    except:
        pass
    return e

'''
This is our trusty data keeper. Instead of losing everything when the terminal closes, 
storage.py handles reading and writing records to local text files (like players.txt 
and scores.txt). It even has built-in safety checks so it won't crash if the files 
don't exist yet.
'''