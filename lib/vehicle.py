class Vehicle:
    pass

    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"
    
    def fill_up_tank(self):
        return "filling up!"


merc = Vehicle(12, 13)
print(merc.wheel_size)
print(merc.wheel_number)
print(merc.go())
print(merc.fill_up_tank())