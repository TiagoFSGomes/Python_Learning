'''
Author: Tiago Gomes
Data: 11/11/2024
Version: 1.0
'''

x = str(3)
y = int(4)
z = float(5)

print(x+x)
print(y+y)
print(z+z)
print('-----------------')

name = 'John Lenon'
age = 36
city = 'Dubai'
print(f'{name} mora em {city} e tem {age} anos!')
print('O ' + name + ' mora em ' + city + ' e tem ' + str(age) + ' anos!')

print('-----------------')

print(type(name))
print(type(age))
print(type(city))

print('-----------------')

# De string para int
num_float = 4.90
nun_int = int(num_float)
print(nun_int)

print('-----------------')

# De int para bool
num_int = 0
is_true = bool(num_int)
print(is_true)

print('-----------------')

num_int = 5
is_true = bool(num_int)
print(is_true)

print('-----------------')

# De string para bool
text = ''
is_true = bool(text)
print(is_true)

print('-----------------')

text = 'Python'
is_true = bool(text)
print(is_true)

print('-----------------')

# De string para lista
text = 'hello'
text_list = list(text)
print(text_list)

print('-----------------')

# De tupla para lista
num_tuple = (1, 2, 3)
num_list = list(num_tuple)
print(num_list)
