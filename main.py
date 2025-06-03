#Import modules from teamfive package
#TODO (ARGUELLES): Import Module
from teamfive.caya import caya_menu
#TODO (CONDINO): Import Module
#TODO (CORDOVA): Import Module
#TODO (GUTIERREZ): Import Module

while True:
    print("=== Team Member Menu ===")
    print("1 - Norlan Arguelles")
    print("2 - Karl Caya")
    print("3 - Ciara Marie Condino")
    print("4 - Aron Stephen Cordova")
    print("5 - King Andrei Gutierrez")
    print("6 - Exit")
    
    choice = input("\nSelect a team member: ")
    
    match choice:
        case "1":
            #TODO (ARGUELLES): Call the appropriate function here
            pass
        case "2":
            caya_menu() 
        case "3":
            #TODO (CONDINO): Call the appropriate function here
            pass
        case "4":
            #TODO (CORDOVA): Call the appropriate function here
            pass
        case "5":
            #TODO (GUTIERREZ): Call the appropriate function here
            pass
        case "6":
            break   
        case _:
            print("Invalid choice. Please try again.")
            