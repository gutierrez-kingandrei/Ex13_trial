import os

def arguelles_menu():
    while True:
        clear_screen()
        print("Good Day! I am Norlan C. Arguelles\n")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comment from Caya")
        print("4. Comment from Condino")
        print("5. Comment from Cordova")
        print("6. Comment from Gutierrez")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        print("")
        
        match choice:
            case "1":
                print("Name: Norlan C. Arguelles")
                print("Date of Birth: December 10, 2004")
                print("Age: 21")
                print("Talents: Singing, Drawing")
                pause()
            case "2":
                print("To be a successful UX/UI Designer.")
                pause()
            case "3":
                print("Keep on dreaming. Padayon!")
                pause()
            case "4":
                print("you LGTM -condino")
                pause()
            case "5":
                print("Hello, I admire your goal.")
                pause()
            case "6":
                # Gutierrez's print comment Placeholder
                pause()
            case "7":
                break
            case _:
                print("Invalid choice, please try again.")
                pause()

def pause():
    input("\nPress Enter to continue...")
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')