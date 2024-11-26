'''
Author: Tiago Gomes
Data: 17/11/2024
Version: 1.0
'''
user_num = int(input('Enter integer number 1-10: '))
user_op = input('Enter an simple arithmetic operator (+, -, *, /): ')


if 1 <= user_num <= 10:
    print('Correct input number')
    for num in range(1, 11, 1):
        if user_op == '+':
            print(f'{user_num}+{num} = {user_num+num}')  # Sum
        elif user_op == '-':
            print(f'{user_num}-{num} = {user_num-num}')  # Subtraction
        elif user_op == '*':
            print(f'{user_num}*{num} = {user_num*num}')  # Multiplication
        elif user_op == '/':  # Division
            s = num * user_num
            print(f'{s}/{user_num} = {s//user_num}')
        else:
            print('Invalid mathematical operation!')
            break  # stop loop1
else:
    print('Error: Input number incorrect')
