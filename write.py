def save_inventory(file_path, inventory):
    with open(file_path, 'w') as file:
        for land in inventory:
            file.write(", ".join(land) + "\n")
