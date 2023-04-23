'''
Write a Python program that iterates the integers from 1 to 50. 
For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". 
For numbers that are multiples of three and five, print "FizzBuzz".
'''

#PROGRAM :

def fizz(i) :

    b = ''

    if i % 3 == 0 :
        b += 'Fizz'

    return b

def buzz(i) :

    c = ''

    if i % 5 == 0 :
        c += 'Buzz'

    return c

def main() :

    a = ''

    for i in range(1,51) :

        b = fizz(i)
        c = buzz(i)

        if b == '' and c == '' :
            a += str(i) + ' '

        else :
            a += b + c + ' '
        
    print(a)

main()