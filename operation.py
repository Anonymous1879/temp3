# operation.py
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
        print("+-----+------------+----------+----+----------+---------------+")
        print("| ID  |  Location  |Direction |Size|  Price   |  Availability |")
        print("+-----+------------+----------+----+----------+---------------+")
        for land in inventory:
            print(f"| {land['kitta_number']:2} | {land['location']:10} | {land['direction']:8} | {land['size']:2} | {land['price']:8.1f} | {land['availability']:13} |")
        print("+-----+------------+----------+----+----------+---------------+")


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

from datetime import datetime

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
            late_duration = input("Enter the late duration: ")
            if update_availability(kitta_number, "Available", inventory):
                kitta_numbers.append((kitta_number, late_duration))
                print("Land returned successfully.")
            else:
                print("Land not found.")

    return kitta_numbers

def update_availability(kitta_number, availability, inventory):
    for land in inventory:
        if land['kitta_number'] == kitta_number:
            land['availability'] = availability
            return True
    return False

def create_invoice(name, action, lands, inventory):
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    invoice_filename = f"{action}_{name}_{current_datetime}.txt"
    invoice_content = f"Invoice for {name} ({action.upper()})\n\n"
    total_amount = 0

    for land in lands:
        kitta_number, duration = land
        for item in inventory:
            if item['kitta_number'] == kitta_number:
                price = item['price']
                if action == "return":
                    total_amount += price * float(duration) * 0.15
                    invoice_content += f"Kitta Number: {kitta_number}, Late Duration: {duration}, Price: {price}, Total: {price * float(duration) * 0.15}\n"
                else:
                    total_amount += price * float(duration)
                    invoice_content += f"Kitta Number: {kitta_number}, Duration: {duration}, Price: {price}, Total: {price * float(duration)}\n"

    invoice_content += f"\nTotal Amount: {total_amount}"
    print(invoice_content)

    with open(invoice_filename, "w") as file:
        file.write(invoice_content)
