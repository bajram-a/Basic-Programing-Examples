"""Write a program that takes from the user a value 'r' that signifies a radius.
The program then calculates the surface area of the circle and its circumference"""

from math import pi

r = float(input())

sur_area = r**2 * pi
cir = 2 * pi * r
