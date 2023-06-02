######## Problem 2 ###############
#Write a program that prints out the Fibonacci sequence up to a given number.
#example 1,2,3,5,8 , next number is the sum of previous two numbers

num=int(input('enter the index value : '))
sequence = ''
c=0
b=1
for i in range(num):    
    sequence += str(c) + ' '
    c+=b
    b=c-b
print(sequence)
#output:
'''
enter the index value : 8
0 1 1 2 3 5 8 13 
'''