'''
Write a Python program to find those numbers which are divisible by 7 and multiples of 5, 
between 1500 and 2700 (both included).
'''

#PROGRAM :

def five(i) :
    
    b = ''
    
    if i % 5 == 0 :
        b = str(i)
    
    return b

def seven(i) :

    c = ''
    
    if i % 5 == 0 :
        c = str(i)
    
    return c

def main() :

    a = ''

    print('Numbers between 1500 & 2700 that r divisible of 5 and 7')

    for i in range(1501,2700) :

        b = five(i)

        if b == '' :
            c = seven(i)

        if b != '' or c != '' :
            a += b + c + ' '

    print(a)

main()