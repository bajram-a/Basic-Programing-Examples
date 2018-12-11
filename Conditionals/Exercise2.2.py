"""Write a program that requiers the user to input two intgers.
The program then prints wether the first one is greater, even or smaller than the second."""

a = int(input())
b = int(input())

if a > b:
    print("It is greater")
elif a == b:
    print("The are equal")
else:
    print("It is smaller")
