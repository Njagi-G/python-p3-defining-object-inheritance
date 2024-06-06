from vehicle import Vehicle

class Car(Vehicle):
    pass

    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"


sedan = Car(10, 25)
print(sedan.wheel_size)
print(sedan.wheel_number)
print(sedan.go())
print(sedan.fill_up_tank())