class Tab:
    menu = {
        'vin': 90,
        'øl': 90,
        'brus': 59,
        'salat': 199,
        'biff': 350,
        'kylling': 329,
        'dessert': 90
    }

    def __init__(self):
        self.total = 0
        self.items = []
        self.day = 0

    def add_item(self, item):
        self.items.append(item)
        self.total += self.menu[item]

    def print_bill(self,tax,tip):
        tax = self.total * tax / 100
        tip = self.total * tip / 100
        total = self.total + tax + tip
        self.day += total

        for item in self.items:
            print(f'{item:20} {self.menu[item]}kr')

        print(f'{"MVA":20} {tax:.2f}kr')
        print(f'{"Tips":20} {tip:.2f}kr')
        print(f'{"Total":20} {total:.2f}kr')
        self.items = []
        self.total = 0
    def print_total_day(self):
        return self.day