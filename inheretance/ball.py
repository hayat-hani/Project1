from math import pi

from inheretance.circle import Circle


class Ball(Circle):
    # def __init__(self, radius):
    #     self.radius = radius

    def volume(self):
        return (4 / 3) * pi * self.radius ** 3

    def area(self):
        return 4 * pi * self.radius ** 2

    def print_area(self):
        print("the area is :", super().area())