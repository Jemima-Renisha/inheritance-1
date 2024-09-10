#main class or parents classs
class vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
#child class
class bus(vehicle):
    pass
#object creation
bus1 = bus("school volvo",130,40)
print("Bus named as:", bus1.name)
