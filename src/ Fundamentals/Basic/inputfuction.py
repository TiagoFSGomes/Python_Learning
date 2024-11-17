'''
Author: Tiago Gomes
Data: 12/11/2024
Version: 1.0
'''

# input é uma função embutida (built-in function),

name = input('Qual seu nome: ')
age = input('Qual sua idade: ')
city = input('Qual sua cidade: ')

print(f'{name} mora em {city} e tem {age} anos!')
print('{x} mora em {y} e tem {z} anos!'.format(x=name, y=city, z=age))
