import random

class Car:
    def __init__(self, reg, top_speed, distance=0):
        self.reg = reg
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance = distance

    def accelerate(self, acceleration):
        if acceleration < 0:
            if self.current_speed + acceleration < 0:
                self.current_speed = 0
            else:
                self.current_speed += acceleration

        elif self.current_speed + acceleration > self.top_speed:
            self.current_speed = self.top_speed

        else:
            self.current_speed += acceleration

    def move(self, hours):
        self.distance = self.distance + self.current_speed * hours

    def print_dist(self):
        print(f"{self.reg} kulki {self.distance} km.")


class Electric(Car):

    def __init__(self, reg, top_speed, battery, distance=0):
        self.battery = battery
        Car.__init__(self, reg, top_speed, distance)


class Combustion(Car):

    def __init__(self, reg, top_speed, tank_size, distance=0):
        self.tank_size = tank_size
        Car.__init__(self, reg, top_speed, distance)


ev = Electric("ABC-15", 180, 52.5)
cv = Combustion("ACD-123", 165, 32.3)

ev.accelerate(random.randint(0, ev.top_speed))
cv.accelerate(random.randint(0, cv.top_speed))

ev.move(3)
cv.move(3)

ev.print_dist()
cv.print_dist()