########## Problem 3 ##########
##buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user. Also get the total number of choc and cakes that the shop has
#Hint - you can buy choc/Cake only if shop has it.

cusBudget = int(input("Enter ur Budget to buy In Bakery : "))
chocCount = int(input("enter the number of chocolate available in shop : "))
cakeCount = int(input("enter the number of cake available in shop : "))
#find how many choc and cake the user can buy.
chocoBought  = int(cusBudget/200)
cakeBought = int(cusBudget/150)
if chocCount<cakeBought :
    chocoBought=chocCount
if cakeCount<cakeBought :
    cakeBought=cakeCount
print(f"The total number of chocolate or cake you can buy is {chocoBought} and {cakeBought}")

#output:
'''
Enter ur Budget to buy In Bakery : 1100
enter the number of chocolate available in shop : 7
enter the number of cake available in shop : 4
The total number of chocolate or cake you can buy is 5 and 4
'''