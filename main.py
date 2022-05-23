import random

length = input('Please enter the length of the passowrd: ')

if length.isdigit():
    length = int(length)
else:
    print('Next time please use integer value as a length')

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
special = '!@#$%^&*()_+-=[]{},.?'

total = lower + upper + numbers + special

password = "".join(random.sample(total, length))

print(password)
