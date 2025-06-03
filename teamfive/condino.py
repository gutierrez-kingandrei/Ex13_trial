import os
def pause():
    input("\nPress Enter to continue...")
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def condino_menu():
    while True:
        clear_screen()
        print("Hello Everyone! I am Ciara Marie Condino")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comment from Arguelles")
        print("4. Comment from Caya")
        print("5. Comment from Cordova")
        print("6. Comment from Gutierrez")
        print("7. Exit")
            
        choice = input("\nEnter your choice: ")
            
        match choice:
            case "1":
                print("I am Ciara Marie Condino and I am 21 years old")
                print("I love playing Grow a Garden in Roblox")
                pause()
            case "2":
                print("My goal is to be a successful daughter and to be rich")
                pause()
            case "3":
                pause()
            case "4":
                pause()
            case "5":
                pause()
            case "6":
                print("Hello, King here!")
                pause()
            case "7":
                break
            case _:
                print("Invalid choice. Please try again.")