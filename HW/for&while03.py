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

print(f"the number of choc and cake are {noOfChoc} and {noOfCake}")
#print no of cakes and choc
#FillinMissingCode