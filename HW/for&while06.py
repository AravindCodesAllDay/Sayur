######## Problem 1 ###############
#write multiplication table like this
# 1 * 1 = 1
# 1 * 2 = 2
#etc. Get the number as input

multiplicationNumber = int (input("enter the number : "))
noOfEntries = int (input("How many rows do you want to print"))

for i in range (1,noOfEntries):
    print (i , "*" , multiplicationNumber , " = ", i*multiplicationNumber)

#output:
'''
enter the number : 4
How many rows do you want to print5
1 * 4  =  4
2 * 4  =  8
3 * 4  =  12
4 * 4  =  16
'''
           
######## Problem 2 ###############
#Write a program that prints out the Fibonacci sequence up to a given number.
#example 1,2,3,5,8 , next number is the sum of previous two numbers

num=int(input('enter the index value : '))
c=1
b=0
for i in range(num):
    c+=b
    print(c)
    b=c-b
#output:
'''
enter the index value : 6
1
2
3
5
8
13
'''

######## Problem 3  ###############
#Write a program that prints out a diamond shape using #.
# Hint - print(5 * "$") will print  - $$$$$
# Hint - print(5* "$ ") will print  - $ $ $ $ $

n = int(input("Enter the number of rows: "))
#print the top triangle
for i in range(n):
    print(" "*(n - i) + "$"*(2*i-1))
#FillinMissingCode for drawing the bottom triangle
for i in range(n - 1, 0, -1):
    print(" "*(n - i) + "$"*(2*i-1))
    
#output:
'''
Enter the number of Characters : 3 
  $ 
 $$$ 
 $$$ 
  $
'''

