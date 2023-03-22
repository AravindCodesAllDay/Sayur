'''
1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit.
'''

#PROGRAM :

#importing time
import time
startTime = time.time()
timeLimit = 10 #in seconds

#initialization cafe items and its properties
cafe = {
    'coffee' : {
        'price' : 40,
        'profit' : 12,
        'stock' : 30,
        'sales' : 0,
        'refill' : 30,
        'totalProfit' : 0
    },
    'tea' : {
        'price' : 35,
        'profit' : 10,
        'stock' : 30,
        'sales' : 0,
        'refill' : 30,
        'totalProfit' : 0
    },
    'cappucino' : {
        'price' : 50,
        'profit' : 14,
        'stock' : 20,
        'sales' : 0,
        'refill' : 20,
        'totalProfit' : 0
    },
    'cookie' : {
        'price' : 30,
        'profit' : 5,
        'stock' : 40,
        'sales' : 0,
        'refill' : 40,
        'totalProfit' : 0
    }
}

quantityInWords = ['one','two','three','four','five','six','seven','eight','nine']
quantityInDigits = ['1','2','3','4','5','6','7','8','9']

def customerOrder(banner) :

    print(banner)

    #getting customer input
    customerInput = input("Enter ur order... : ")

    #returning customer input as a list
    return customerInput.lower().split()

#getting customer input and calculating the sold items
def processCustomerInput(list1) :
        
    totalCost = 0

    #taking the input and filtering values
    for i,items in enumerate(cafe.keys()) :

        quantities = 0
        
        if items in list1:
            
            index = list1[list1.index(items) - 1]

            if index in quantityInWords :
                quantities =  quantityInWords.index(index) + 1

            elif index in quantityInDigits :
                quantities =  quantityInDigits.index(index) + 1

        #checking the items left to provide or restock
        refill(items,quantities)
                    
        #updating the stock and sales
        cafe[items]['stock'] -= quantities
        cafe[items]['sales'] += quantities
        cafe[items]['totalProfit'] += (quantities * cafe[items]['profit'])

        #displaying the price of the items buyed
        if quantities != 0 :

            print(f'{items.capitalize()} Cost = {cafe[items]["price"] * quantities}')

        #calculating the total bill to be paid
        totalCost += (cafe[items]['price'] * quantities)
           
    print(f'Total bill = {totalCost}')

def refill(items,quantities) :

    #stock refill checking conditions
    if (cafe[items]['stock'] <= (cafe[items]['refill'] * 0.2)) or (cafe[items]['stock'] - quantities < 0) :
    
        cafe[items]['stock'] = cafe[items]['refill']
        print(f"{items} Refilled....")

def topItemsCategory() :

    topSales = {
        'coffee' : cafe['coffee']['sales'],
        'tea' : cafe['tea']['sales'],
        'cappucino': cafe['cappucino']['sales'],
        'cookie': cafe['cookie']['sales']
    }

    topProfit = {
        'coffee' : cafe['coffee']['totalProfit'],
        'tea' : cafe['tea']['totalProfit'],
        'cappucino': cafe['cappucino']['totalProfit'],
        'cookie': cafe['cookie']['totalProfit']
    } 

    #sorting the top sales and profit
    sortedTopSales = sorted(topSales.items(),key=lambda x:x[1],reverse=True)[:3]
    sortedTopProfit = sorted(topProfit.items(),key=lambda x:x[1],reverse=True)[:3]

    print("\nTop 3 Sales items")
    for x in sortedTopSales :

        print(f'{x[0]}-{x[1]}')

    print("\nTop 3 Profit items")
    for x in sortedTopProfit :

        print(f'{(x[0])}-{x[1]}')

def main() :

    print("\t...Welcome to the cafe..")
    print("(Here are the items that we can serve)")
    banner = ''

    #displaying items
    for i,item in enumerate(cafe.keys()) :

        banner += '\n' + str(i+1) + ' - ' + str(item.upper())

    #checking time duration
    while (time.time() - startTime) < timeLimit :    

        #getting input 
        list1 = customerOrder(banner)

        #calling function to process customer input
        processCustomerInput(list1)

    #calling function to print top results 
    topItemsCategory()

    #refilling the stock
    for z in cafe.values() :
            
        z['stock'] = z['refill']
        
    print("All items Refilled....")

main()