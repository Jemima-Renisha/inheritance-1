#main class or parents classs
class vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
    def show(self):
        print("Bus named as",self.name)

#child class
class bus(vehicle):
    def __init__(self,name,maxspeed,mileage,color):
        self.color = color
        vehicle.__init__(self, name, maxspeed, mileage)
#object creation
x = bus("school volvo",130,45,"red")
x.show()
print("color is",x.color)

