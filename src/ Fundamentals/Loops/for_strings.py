'''
Author: Tiago Gomes
Data: 17/11/2024
Version: 1.0
'''
word_list = ['banana', 'apple', 'avocate', 'vegetables', 'bacon', 'tomatoes']

for word in word_list:
    if word == 'avocate':
        print(word)

print('--------------------------------')

for word in word_list:
    if word.startswith('t'):  # string.startswith(value, start, end)
        print(word)


print('--------------------------------')

print(f'This is original list {word_list}')
for word in word_list[:]:  # Shallow Copy
    if word == 'banana':
        word_list.remove(word)  # Modified original list - remove banan
        new_list = word_list
        print(f'Modified list {word_list}')
