'''
Author: Tiago Gomes
Data: 16/11/2024
Version: 1.0
'''

message = 'i like food with Bacon'

# Python - Modify Strings
print(message.lower())
print(message.upper())
print(message.capitalize())


print(message.find('i'))
print(message.find('B'))
print(message.find('Bacon'))

# Replace String
print(message.replace('i', 'o'))
print(message.replace('Bacon', 'Vegetables'))

# Split String
txt0 = 'Hi, Pyhton'
print(txt0.split(','))

# Remove Whitespace
txt1 = '        ,,,,,rrttgg.....       banana....rrr'
print(txt1.strip(' ,.rtg'))

txt2 = "     banana     "
x = txt2.rstrip()
print("of all fruits", x, "is my favorite")

print('|'.join(message))

txt3 = "Company10"
print(txt3.isalnum())
print(txt3.isalpha())
print(txt3.isdigit())


fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

txt4 = 'apple'
print(txt4.index('a'))
print(txt4.index('l'))
