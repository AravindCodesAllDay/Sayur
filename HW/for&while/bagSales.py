 ########## Problem 3 ############
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold

#initialize variables
redBags, whiteBags = 100, 200
totalSales, totalBagsSold = 0, 0

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
print (f"totalSales amount = {totalSales}")

#output:
'''
enter the amount of red bags needed : 25
enter the amount of white bags needed : 30
totalBagsSold = 55
totalSales amount = 70000
'''