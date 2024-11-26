'''
Author: Tiago Gomes
Data: 17/11/2024
Version: 1.0
'''
user_num = int(input('Enter integer number: '))
ratio = int(input('Enter a ratio: '))

# a10 = a1 + (10 -1) * r
a10 = user_num + (10-1) * ratio
print(f'Tenth term is: {a10}')

for c in range(user_num, a10 + 1, ratio):
    print(c)
