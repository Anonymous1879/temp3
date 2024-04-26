class Land:
    def __init__(self, kitta_number, city, direction, anna, price, availability):
        self.kitta_number = kitta_number
        self.city = city
        self.direction = direction
        self.anna = anna
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"{self.kitta_number}, {self.city}, {self.direction}, {self.anna}, {self.price}, {self.availability}"

    @staticmethod
    def parse_land_from_line(line):
        fields = line.strip().split(", ")
        return Land(*fields)
