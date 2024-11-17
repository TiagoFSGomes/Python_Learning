'''
Author: Tiago Gomes
Data: 16/11/2024
Version: 1.0
'''

'''
How It Works:

Input treated with strip() and lower():

Removes unnecessary spaces at the beginning and end of the string.
Converts input to lowercase, ensuring that "True", "true" or " TRUE " are interpreted the same way.
Explicit check (== 'true'):

Converts the text "true" to True and any other input to False.
'''

income = input(
    'Type True or False for fixed income: ').strip().lower() == 'true'
no_pending = input(
    'Type True or False for no pending: ').strip().lower() == 'true'

income_fixed = int(input('Type your fixed monthly income in dollars: '))

income_base = 5000

print(type(income))
print(type(no_pending))

if income and no_pending and income_fixed >= income_base:
    print('Financing accepted')
elif income or no_pending or income_fixed >= income_base:
    print('Financing pending bank approval')
else:
    print('Financing denied')
