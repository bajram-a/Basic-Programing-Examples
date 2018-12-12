"""Write a program that requires a user to input a sentence, which
the program then prints out the words backwards/in reverse """

string = input()
string += ' '
output = ''

word = ''

for i in range(len(string)):

    if string[i] == ' ':
        output = word + ' ' + output
        word = ''
    else:
        word += string[i]

print(output)
