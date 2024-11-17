'''
Author: Tiago Gomes
Data: 16/11/2024
Version: 1.0
'''
if (speed := int(input('Enter a speed value: '))) >= 110:
    print('Speed Limit Exceeded')
elif speed < 60:
    print('Speed below the permitted limit')
else:
    print('Speed OK')
