# main.py
from read import  read_inventory
import operation

def main():
    print("Welcome to TechnoPropertyNepal")
    inventory = read_inventory("inventory.txt")

    while True:
        choice = operation.get_user_choice()

        if choice == "1":
            operation.display_inventory(inventory)
        elif choice == "2":
            operation.perform_rent(inventory)
        elif choice == "3":
            operation.perform_return(inventory)
        elif choice == "4":
            print("Thank you for using TechnoPropertyNepal. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()