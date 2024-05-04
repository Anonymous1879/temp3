# read.py
def read_inventory(file_path):
    inventory = []
    with open(file_path, 'r') as file:
        for line in file:
            fields = line.strip().split(", ")
            land = {
                "kitta_number": fields[0],
                "location": fields[1],
                "direction": fields[2],
                "size": int(fields[3]),
                "price": float(fields[4]),
                "availability": fields[5]
            }
            inventory.append(land)
    return inventory