from players import x, z
from scores import a, b
from test import runalltests

def main():
    """Execute the primary command-line interface loop for the application."""
    while True:
        print("\n           RETRO ARCADE & PLAYER VAULT       ")
        print()
        print("             1--> Register new player")
        print("             2--> View all players")
        print("             3--> View high scores")
        print("             4--> Submit a high score")
        print("             5--> Run Unit Tests")
        print("             6--> Exit")
        print("")
        choice = input("Enter your choice (1-6): ").strip()
        if choice=="1":
            x()
        elif choice=="2":
            z()
        elif choice=="3":
            b()
        elif choice=="4":
            a()
        elif choice=="5":
            runalltests()
        elif choice=="6":
            print("\nExiting program.")
            break
        else:
            print("Invalid choice. Choose btw 1 and 6.")

if __name__ == "__main__":
    main()
