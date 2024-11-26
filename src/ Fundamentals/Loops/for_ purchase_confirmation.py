'''
Author: Tiago Gomes
Data: 17/11/2024
Version: 1.0
'''
user_email = input('Enter your personal e-mail: ')

conf = input(
    'Type True or False purchase confirmation: ').strip().lower() == 'true'

summary = 'Purchase worth 12.50 was delivered'

for attempt in range(3):
    if conf:  # if the purchase confirmation is true
        print(summary)
        print(f'Purchase summary sent to email {user_email}')
        break  # stop loop
else:
    print('Purchase failure')
