class Human:
    def __init__(self, name):
        self.name = name

class Auto:
    def __init__(self, brand, num_seats):
        self.brand = brand
        self.passengers = []
        self.num_seats = num_seats

    def add_passenger(self, human):
        if len(self.passengers) >= self.num_seats:
            print(f"В машині {self.brand} немає місць для нового пасажира {human.name}!!!")
        else:
            self.passengers.append(human)

    def print_passengers(self):
        if self.passengers != []:
            print(f"В машині {self.brand} такі пасажири:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"В машині {self.brand} немає пасажирів. Всі втікли!")

car = Auto('Nissan GTR', 4)
car.add_passenger(Human("Oleg"))
car.add_passenger(Human("Igor"))
car.add_passenger(Human("Vlad"))
car.add_passenger(Human("Adrian"))
car.add_passenger(Human("Artur"))
car.print_passengers()

