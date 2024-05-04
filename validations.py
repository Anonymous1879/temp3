# validations.py
def validate_menu_selection(selection):
    try:
        selection = int(selection)
        if selection < 1 or selection > 4:
            return "Invalid menu selection. Please enter a number between 1 and 4."
        else:
            return None
    except ValueError:
        return "Invalid Input"

def validate_land_id(land_id, action, inventory):
    try:
        land_id = int(land_id)
        if land_id <= 0:
            return "Input positive numbers"
        elif not any(land['kitta_number'] == str(land_id) for land in inventory):
            return "Land ID does not exist"
        elif action == "rent" and not any(land['kitta_number'] == str(land_id) and land['availability'] == "Available" for land in inventory):
            return "Land ID is not available for rent"
        elif action == "return" and not any(land['kitta_number'] == str(land_id) and land['availability'] == "Not Available" for land in inventory):
            return "Land ID is not currently rented"
        else:
            return None
    except ValueError:
        return "Invalid Input"


def validate_duration(duration, action):
    try:
        duration = int(duration)
        if duration < 0:
            return "Input positive numbers"
        elif duration == 0 and action == "rent":
            return "Duration must be greater than 0"
        else:
            return None
    except ValueError:
        return "Invalid Input"



def validate_name(name):
    if any(char.isdigit() for char in name):
        return "Invalid Input, Name cannot contain numbers"
    else:
        return None