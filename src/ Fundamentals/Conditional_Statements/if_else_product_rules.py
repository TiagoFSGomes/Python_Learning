'''
Author: Tiago Gomes
Data: 16/11/2024
Version: 1.0
'''
if (value_product := int(input('Enter value product: '))) and 20 <= value_product <= 40:
    print('Accepted product')
else:
    print('Product denied')
