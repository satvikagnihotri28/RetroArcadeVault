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