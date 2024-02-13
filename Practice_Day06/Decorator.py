speed = property()
# speed = speed.getter(speed, get_speed)
# spped = speed.setter(speed, set_speed)

class Car:
    def __init__(self, speed = 40):
        self.speed = speed 
        return 
    @property
    def speed(self):
        return self.speed
    def speed(self, speed):
        if 0 < speed > 100:
            print("It is in 0 to 100 ")
            return 
        self.speed = speed
        return
c1 = Car()
print(c1.speed)
c1.speed = 110
print(c1.speed)

