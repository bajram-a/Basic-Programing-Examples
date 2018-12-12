"""Write a program that takes a whole number n as a parameter, the program
then prints True if its a rime number, and False if its not.

*A prime number (or a prime) is a natural number greater than 1 that
cannot be formed by multiplying two smaller natural numbers."""

n = int(input())

prime = True
divisions = 0

for i in range(1, n):

    if n % (i + 1) == 0:
        divisions += 1

    if divisions == 2:
        prime = False
        break
if n == 1:
    prime = False

print(prime)