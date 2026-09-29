def y(nn, e):
    """Write a list of data entries to a specified text file."""
    try:
        file = open(nn, "w")
        for item in e:
            file.write(item+"\n")
        file.close()
    except:
        print("Can not save to file...")
def q(nn):
    """Read and return lines from a specified text file, handling missing files safely."""
    e = []
    try:
        file = open(nn, "r")
        for line in file:
            e.append(line.strip())
        file.close()
    except:
        pass
    return e