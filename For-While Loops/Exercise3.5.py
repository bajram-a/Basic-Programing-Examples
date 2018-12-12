"""Write a program that takes a string (word or sentence) as an input
 parameters, as long as the user doesn't input an empty string.
 The program then prints out the number of letters 'a" used in those strings.
 *The program SHOULD NOT differentiate between capital and lowercase letters"""

string = ' '
a = 0

while string != '':
    string = input()
    for i in range(len(string)):
        if string[i].lower() == 'a':
            a += 1

print(a)