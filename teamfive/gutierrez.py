import os

def gutierrez_menu():
    
    while True:
        clear_screen()
        print("Hello, I am King Andrei Gutierrez")
        print("1 - Basic Information")
        print("2 - Goals")
        print("3 - Comment from Arguelles")
        print("4 - Comment from Caya")
        print("5 - Comment from Condino")
        print("6 - Comment from Cordova")
        print("7 - Exit")
        
        choice = input("\nSelect a team member: ")
        
        match choice:
            case "1":
                print("-Basic Information-")
                print("Name: King Andrei B. Gutierrez")
                print("Age: 20")
                print("Birthday: February 21, 2005")
                pause()
            case "2":
                print("Goal: To be successful in life and career.")
                pause()
            case "3":
                #Comment from Arguelles
                pass
            case "4":
                print("Keep on dreaming. Padayon!")
            case "5":
                print("you LGTM -condino")
                pass
            case "6":
                print("Hello, I admire your goal.")
                pass 
            case "7":
                break   
            case _:
                print("Invalid choice. Please try again.")
 
def pause():
    input("\nPress Enter to continue...")
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')               
                
                