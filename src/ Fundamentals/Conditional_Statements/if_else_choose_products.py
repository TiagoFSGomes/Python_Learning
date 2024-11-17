'''
Author: Tiago Gomes
Data: 16/11/2024
Version: 1.0
'''

print('Welcome! Choose yours products!')
print('--------------Catalog--------------------')
print('1}P1\n2}P2\n3}P3\n4}P4\n5}P5')
print('-----------------------------------------')
p = int(input('Enter the product number: '))

if p == 1:
    print('You selected product 1')
elif p == 2:
    print('You selected product 2')
elif p == 3:
    print('You selected product 3')
elif p == 4:
    print('You selected product 4')
elif p == 5:
    print('You selected product 5')
else:
    print('Invalid choice')
