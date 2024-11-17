'''
Author: Tiago Gomes
Data: 16/11/2024
Version: 1.0
'''

c = input('Enter single alphabet or digit: ')
if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
    print('Lower case vowel')
elif c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
    print('Upper case vowel')
elif '0' <= c <= '9':
    print('Digit')
else:
    print('Consonant')
