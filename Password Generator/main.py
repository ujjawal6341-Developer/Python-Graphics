import random 

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$&'

lenght = int(input('Enter Length : '))

password = ''

for a in range(lenght):
    password+=random.choice(char)
print(password)    

