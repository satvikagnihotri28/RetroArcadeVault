def t(pp):
    while True:
        value = input(pp).strip()
        if value:
            return value
        print("Error..Input can't be empty. Try again.....")
def w(pp):
    while True:
        value = input(pp).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Error;enter a valid positive number.")

'''
Meet our friendly input bouncer! helpers.py is packed with utility functions 
that sanitize what the user types. It uses loops to make sure nobody submits 
blank text and that scores are always valid positive numbers before processing.
'''