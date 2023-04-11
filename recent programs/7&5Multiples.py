'''
Write a Python program to find those numbers which are divisible by 7 and multiples of 5, 
between 1500 and 2700 (both included).
'''

#PROGRAM :

a = ''

print('Numbers between 1500 & 2700 that r divisible of 5 and 7')

for i in range(1500,2700) :

    if i % 5 == 0 and i % 7 == 0 :
        a += str(i) + '  '

print(a)