'''
Author: Tiago Gomes
Data: 16/11/2024
Version: 1.0
'''

print('Welcome! Type two numbers and select the mathematical operation!')

number1 = float(input('Type number 1: '))
number2 = float(input('Type number 2: '))
operator = input('Enter an arithmetic operator (+, -, *, **, /, //, %): ')

if operator == '/':
    # Avoid division by zero
    if number2 == 0:
        print('Error: Division by zero is not allowed!')
    else:
        print('Inter quotient=', number1 / number2)

elif operator == '+':
    print('Sum=', number1+number2)
elif operator == '-':
    print('Substraction=', number1-number2)
elif operator == '*':
    print('Product=', number1*number2)
elif operator == '**':
    print('Power=', number1**number2)
elif operator == '//':
    print('Float quotient=', number1//number2)
elif operator == '%':
    print('Reaminder=', number1 % number2)
else:
    print('Invalid Operator')
