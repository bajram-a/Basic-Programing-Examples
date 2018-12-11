"""Write a program that requires the user to input the length of two sides of a triangle.
The program then calculates the required length of the third side(hypotenuse) for the triangle
to be a right angle one.
*round the value to two decimals"""

from math import sqrt

a = float(input())
b = float(input())

c = sqrt(a**2 + b**2)

