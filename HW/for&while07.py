######## Problem 1 ###############
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines

n = int(input("Enter the number of rows: "))
#print the top triangle
for i in range(n):
    a =input()
    if a!=' ':
        break
    print(" "*(n - i) + "$"*(2*i-1))

for i in range(n - 1, 0, -1):
    if a != ' ' :
        break
    a=input()
    print(" "*(n - i) + "$"*(2*i-1))
    

######## Problem 2 ###############
# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly 
# https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number

import random#FillinMissingCode
computerNo = random.randint(3, 9)
attempt = 0
while(True):
    userNo = int (input("Enter ur guess"))
    #FillinMissingCode
    attempt +=1
    if userNo == computerNo:
        print(f"u found the number {computerNo} in attempt {attempt}")
        break
    elif userNo > computerNo:
        print('Lower')
        continue
    print('Higher')
    
########## Problem 3 ############
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold

#initialize variables
redBags, whiteBags = 100, 200
totalSales , totalBagsSold = 0

while (totalSales < 10000 or totalBagsSold < 10) :
    #Ask customer for input
    redbag = int(input('enter the amount of red bags needed : '))
    whitebag = int(input('enter the amount of white bags needed : '))
    #FillinMissingCode
    
    #calculate total cost for the bags
     #FillinMissingCode
    totalSales +=  (1000*redbag)+(1500*whitebag)
    #increment no of bags sold
    totalBagsSold += redbag + whitebag #FillinMissingCode

print (f"totalBagsSold = {totalBagsSold}") #FillinMissingCode) 
print (f"totalSales = {totalSales}")