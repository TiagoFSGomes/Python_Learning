'''
Author: Tiago Gomes
Data: 17/11/2024
Version: 1.0
'''
user_phrase = input('Enter your phrase: ').strip().upper()
print(user_phrase)

words = user_phrase.split()  # list of words
print(words)

fusion_words = ''.join(words)
print(fusion_words)


inverse = ''

for letter in range(len(fusion_words) - 1, -1, -1):
    inverse += fusion_words[letter]

print(f'Inverse: {inverse} : Fusion Words: {fusion_words}')

if inverse == fusion_words:
    print('This is palidrome')
else:
    print('This is not a palidrome')
