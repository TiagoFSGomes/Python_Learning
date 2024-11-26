'''
Author: Tiago Gomes
Data: 17/11/2024
Version: 1.0
'''
s = 0
for num in range(1, 10, 1):
    if (num % 3) == 0:
        print(num)
        s += num  # s = s + num
print('Finish!')
print(f'The sum of all values is: {s}')
