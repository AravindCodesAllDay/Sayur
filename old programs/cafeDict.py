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
    for item in list1:
        
        #checking the item in cafe
        if item in cafe.keys():
            
            #looping to find the quantity for the item
            for i,quantities in enumerate(list1):
                
                #checking for the quantity
                if quantities.isnumeric():

                    quantities =int(quantities)
                    #refill checking function
                    refill(item,quantities)
                    #updating the sales quantity and total profit
                    cafe[item]['sales'] += quantities
                    cafe[item]['stock'] -= quantities
                    cafe[item]['totalProfit'] += cafe[item]['profit']*cafe[item]['sales']

                    #displaying the price of the items buyed
                    if quantities != 0 :

                        print(f'{item.capitalize()} Cost = {cafe[item]["price"] * quantities}')

                    #calculating the total bill to be paid
                    totalCost += (cafe[item]['price'] * quantities)
                    list1[i] = 'a'
                    break      
                  
    print(f'Total bill = {totalCost}')

def refill(item,quantities) :

    #stock refill checking conditions
    if (cafe[item]['stock'] <= (cafe[item]['refill'] * 0.2)) or (cafe[item]['stock'] - quantities < 0) :
    
        cafe[item]['stock'] = cafe[item]['refill']
        print(f"{item} Refilled....")

def topItemsCategory() :

    #sorting the top sales and profit
    topSales = dict(sorted(cafe.items(),key=lambda x:x[1]['sales'],reverse=True)[:3])
    topProfit = dict(sorted(cafe.items(),key=lambda x:x[1]['totalProfit'],reverse=True)[:3])

    print("\nTop 3 Sales items")
    for x in topSales :

        print(f'{x}-{topSales[x]["sales"]}')

    print("\nTop 3 Profit items")
    for x in topProfit :

        print(f'{x}-{topProfit[x]["totalProfit"]}')

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