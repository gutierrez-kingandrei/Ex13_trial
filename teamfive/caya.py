from os import system

def clear():
    system("cls")
    
def getch():
    enter = input("\nPlease enter to continue...")

def caya_menu():
    while True:
        clear()
        print("----------Welcome to Caya's Menu----------")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Comment from Arguelles")
        print("4. Comment from Condino")
        print("5. Comment from Cordova")
        print("6. Comment from Gutierrez")
        print("0. Exit")
        
        choice = input("\nPlease enter your choice: ")
        
        match choice:
            case "1":
                clear()
                print("----------Basic Information----------")
                print("Name: Karl Christian M. Caya")
                print("Age: 20 years old")
                print("Date of Birth: December 7, 2004")
                print("Gender: Male")
                getch()
            case "2":
                clear()
                print("----------------------Goals----------------------")
                print("- I want to graduate with flying colors.")
                print("- Find a decent job that will support my family.")
                print("- I want to travel the world.")
                getch()
            case "3":
                clear()
                print("Keep up the good work, Caya!")
                getch()  
            case "4":
                clear()
                print("you LGTM -condino")
                getch() 
            case "5":
                clear()
                print("Hello, I admire your goal.")
                getch()
            case "6":
                clear()
                print("Hello, King here!")
                getch()    
            case "0":
                break
            case _:
                print("\nInvalid choice. Try again!")
                getch()