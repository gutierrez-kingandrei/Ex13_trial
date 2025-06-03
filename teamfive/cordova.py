import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def buffer():
    input("\nPress Enter to return to the menu")

def cordova_menu():
    while True:
        clear()
        print("\nBonjour! Je suis Aron Stephen S. Cordova")
        print("\n1. About me")
        print("2. My goals")
        print("3. Comment from Arguelles")
        print("4. Comment from Caya")
        print("5. Comment from Condino")
        print("6. Comment from Gutierrez")
        print("7. Exit menu")

        choice = input("\nEnter your choice: ")

        clear()

        match choice:
            case "1":
                print("Name: Aron Stephen S. Cordova")
                print("Age: 20 years old")
                print("Birthdate: March 3, 2005")
                buffer()
            case "2":
                print("Goal: Graduate")
                buffer()
            case "3":
                print("Let's go, Aron! Keep it up!")
                buffer()
            case "4":
                buffer()
            case "5":
                print("you LGTM -condino")
                buffer()
            case "6":
                buffer()
            case "7":
                break
            case _:
                print("\nInvalid choice.")
                buffer()
                