"""Write a program that requires the user to input four real numbers. The program then prints
the smallest one."""

a = float(input())
b = float(input())
c = float(input())
d = float(input())

min = a

if b < min:
    min = b

if c < min:
    min = c

if d < min:
    min = d

print(min)