"""Write a program that requires from the user to input coordinates x and y for the circle center
and the radius of that circle, then another set of coordinates for point A.
The program then calculates whether A is within the circle"""

from math import sqrt

Cir_x = float(input())
Cir_y = float(input())

r = float(input())

Ax = float(input())
Ay = float(input())

d = sqrt((Ax - Cir_x)**2 + (Ay - Cir_y)**2)

if d <= r:
    print("A is within the circle")
else:
    print("A isn't within the circle")
