from read import read_inventory
from write import save_inventory
from datetime import datetime

def get_user_choice():
    print("\nMenu:")
    print("1. See Inventory")
    print("2. Rent")
    print("3. Return")
    print("4. Exit")
    return input("Please enter your choice (1-4): ")

def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for land in inventory:
            print(land)

def perform_rent(inventory):
    rented_lands = get_kitta_numbers("rent", inventory)
    if rented_lands:
        name = get_name()
        create_invoice(name, "rent", rented_lands, inventory)
        save_inventory("inventory.txt", inventory)

def perform_return(inventory):
    returned_lands = get_kitta_numbers("return", inventory)
    if returned_lands:
        name = get_name()
        create_invoice(name, "return", returned_lands, inventory)
        save_inventory("inventory.txt", inventory)

def get_name():
    return input("Enter your name: ")

def get_kitta_numbers(action, inventory):
    kitta_numbers = []
    while True:
        kitta_number = input(f"Enter the kitta number of the land to {action} (or 'done' to finish): ")
        if kitta_number.lower() == "done":
            break
        if action == "rent":
            duration = input("Enter the rental duration: ")
            if update_availability(kitta_number, "Not Available", inventory):
                kitta_numbers.append((kitta_number, duration))
                print("Land rented successfully.")
            else:
                print("Land not found.")
        else:
            if update_availability(kitta_number, "Available", inventory):
                kitta_numbers.append(kitta_number)
                print("Land returned successfully.")
            else:
                print("Land not found.")

    return kitta_numbers

def update_availability(kitta_number, availability, inventory):
    for land in inventory:
        if land[0] == kitta_number:
            land[5] = availability
            return True
    return False

def create_invoice(name, action, lands, inventory):
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    invoice_filename = f"{action}_{name}_{current_datetime}.txt"
    invoice_content = f"Invoice for {name} ({action.upper()})\n\n"

    for land in lands:
        if action == "rent":
            kitta_number, duration = land
            invoice_content += f"Kitta Number: {kitta_number}, Duration: {duration}\n"
        else:
            kitta_number = land
            invoice_content += f"Kitta Number: {kitta_number}\n"

    with open(invoice_filename, "w") as file:
        file.write(invoice_content)

    print(f"Invoice generated: {invoice_filename}")

