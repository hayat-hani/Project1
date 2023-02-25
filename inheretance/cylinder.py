from math import pi

from inheretance.circle import Circle


class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def volume(self):
        return pi * self.radius ** 2 * self.height

    def area(self):
        return self.cir() * self.height

    def get_base(self):
        return super() #return circle object

    def area_of_base(self):
        return super().area()