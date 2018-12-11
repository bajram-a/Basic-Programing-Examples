"""Write a program that takes the values 'a', 'b', and 'c' as real numbers
from the user. The program then calculates the surface area of a triangle
whose sides are a, b and c"""

from math import sqrt

a = float(input())
b = float(input())
c = float(input())

s = (a + b + c) / 2 # semiperimeter
sur_area = sqrt(s * (s - a) * (s - b) * (s - c))

