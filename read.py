def read_inventory(file_path):
    inventory = []
    with open(file_path, 'r') as file:
        for line in file:
            fields = line.strip().split(", ")
            inventory.append(fields)
    return inventory
