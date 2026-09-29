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
def t(pp):
    """Prompt the user for input and ensure the string is not empty."""
    while True:
        value = input(pp).strip()
        if value:
            return value
        print("Error..Input can't be empty. Try again.....")
def w(pp):
    """Prompt the user for input and validate that it is a positive integer."""
    while True:
        value = input(pp).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Error;enter a valid positive number.")