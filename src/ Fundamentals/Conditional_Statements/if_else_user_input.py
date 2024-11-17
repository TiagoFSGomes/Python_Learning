'''
Author: Tiago Gomes
Data: 16/11/2024
Version: 1.0
'''

if (user_input := input('Type something: ')) and len(user_input) >= 3:
    print(f'The text "{user_input}" entered has {len(user_input)} characteres')
else:
    print('The value entered has less than 3 characters')
