#Import modules from teamfive package
from teamfive.arguelles import arguelles_menu
#TODO (CAYA): Import Module
#TODO (CONDINO): Import Module
from teamfive.cordova import cordova_menu
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
            #TODO (CAYA): Call the appropriate function here
            pass
        case "3":
            #TODO (CONDINO): Call the appropriate function here
            pass
        case "4":
            cordova_menu()
            
        case "5":
            #TODO (GUTIERREZ): Call the appropriate function here
            pass
        case "6":
            break   
        case _:
            print("Invalid choice. Please try again.")
            