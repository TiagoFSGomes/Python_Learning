'''
Author: Tiago Gomes
Data: 16/11/2024
Version: 1.0
'''

x = 10
x += 5  # x = x+5
print(x)

y = 15
y -= 5  # = y-5
print(y)

z = 21
z /= 3  # z = z / 3
print(z)

w = 2
w *= 3  # w  = w * 3
print(w)

k = 2
k **= 8  # w  = w ** 3 = 256
print(k)

j = 10
j %= 6  # 10/6 = 4
print(j)

l = 10
l //= 3
print(l)

# operator "walrus :="
# Assigns the value to a variable while evaluating an expression.

# value = input("Type a value: ")
# if len(value) > 5:
#   print('The value is greater than 5 characters!')

if (value := input("Type a value:: ")) and len(value) > 5:
    print('The value is greater than 5 characters!')
