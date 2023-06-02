#buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user.

#find how many choc and cake the user can buy

noOfCake = 0
noOfChoc = 0
#get budget
money = int(input("enter your budget : "))
#FillinMissingCode
money1 = money

while (money >= 200 or money1 >=150) : 

    if (money >= 200) :
        #buy choc
        noOfChoc += 1
        money -= 200

    noOfCake += 1
    money1 -= 150    
    #FillinMissingCode for buying cake

print(f"the number of chocolates and cakes you can buy are {noOfChoc} and {noOfCake}")
#print no of cakes and choc
#FillinMissingCode

#output:
'''
enter your budget : 1100
the number of chocolates and cakes you can buy are 5 and 7
'''
