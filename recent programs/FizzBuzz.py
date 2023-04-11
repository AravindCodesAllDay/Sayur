'''
Write a Python program that iterates the integers from 1 to 50. 
For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". 
For numbers that are multiples of three and five, print "FizzBuzz".
'''

#PROGRAM :

a = ''

for i in range(1,51) :

    if i % 3 == 0 and i % 5 == 0 :
        a += 'FizzBuzz  '

    elif i % 3 == 0 :
        a += 'Fizz  '

    elif i % 5 == 0 :
        a += 'Buzz  '
        
    else :
        a += str(i) + '  '

print(a)
