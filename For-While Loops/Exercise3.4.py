"""Write a program that requires the user to input a whole number n,
the program then 'draws' a triangle using the symbol '*'
Example:

    Input: 5
    Output: *
            **
            ***
            ****
            *****
    """

n = int(input())

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print( )