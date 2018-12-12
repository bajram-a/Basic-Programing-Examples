"""Write a program that takes DNA sequences and interprets them as RNA
sequences
*DNA sequence is made up of A, C, G, T
*RNA sequence is made up of A, C, G , U
G -> C
C -> g
T -> A
A -> U"""


a = input()
output = ''
for i in range(0, len(a)):
    nuk = a[i]
    if nuk == 'A':
        b += 'U'
    elif nuk == 'T':
        b += 'A'
    elif nuk == 'C':
        b += 'G'
    elif nuk == 'G':
        b += 'C'

print(ourput)