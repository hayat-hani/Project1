from inheretance.ball import Ball
from inheretance.cylinder import Cylinder

b_1 = Ball(1)
print(b_1.volume())
b_1.print_area()

cy = Cylinder(4, 20)
print(cy.area())
print(cy.cir())
print(cy.get_base().area())