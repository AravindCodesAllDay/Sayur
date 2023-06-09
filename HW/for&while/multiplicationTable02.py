######## Problem 1 ###############
#write multiplication table like this
# 1 * 1 = 1
# 1 * 2 = 2
#etc. Get the number as input

multiplicationNumber = int (input("enter the number : "))
noOfEntries = int (input("How many rows do you want to print : "))

for i in range (1,noOfEntries):
    print (i , "*" , multiplicationNumber , " = ", i*multiplicationNumber)

#output:
'''
enter the number : 4
How many rows do you want to print : 5
1 * 4  =  4
2 * 4  =  8
3 * 4  =  12
4 * 4  =  16
'''
