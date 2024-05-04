# write.py
def save_inventory(file_path, inventory):
    with open(file_path, 'w') as file:
        for land in inventory:
            file.write(", ".join(str(land[key]) for key in land) + "\n")
