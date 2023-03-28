'''
Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit.

Extension of Cafe
    1 Replenish supply for every 5 customers  and at the end of the day

    2 Calculate replenish supply at the starting of the day for hot items, 
      every 5 customers for all items and only cold items  at the every end of the day.
'''

#PROGRAM :

#importing time
import time
startTime = time.time()
timeLimit = 30 #in seconds

#initialization cafe items and its properties
cafe = {
    'coffee' : {
        'price' : 40,
        'profit' : 12,
        'stock' : 30,
        'sales' : 0,
        'refill' : 30,
        'totalProfit' : 0,
        'category' : 'hot'
    },
    'tea' : {
        'price' : 35,
        'profit' : 10,
        'stock' : 30,
        'sales' : 0,
        'refill' : 30,
        'totalProfit' : 0,
        'category' : 'hot'
    },
    'cappucino' : {
        'price' : 50,
        'profit' : 14,
        'stock' : 20,
        'sales' : 0,
        'refill' : 20,
        'totalProfit' : 0,
        'category' : 'hot'
    },
    'cookie' : {
        'price' : 30,
        'profit' : 5,
        'stock' : 40,
        'sales' : 0,
        'refill' : 40,
        'totalProfit' : 0,
        'category' : 'cold'
    },
    'cake' : {
        'price' : 50,
        'profit' : 10,
        'stock' : 35,
        'sales' : 0,
        'refill' : 35,
        'totalProfit' : 0,
        'category' : 'cold'
    }
}

refillCount = 0

def customerOrder(banner) :

    print(banner)

    #getting customer input
    customerInput = input("Enter ur order... : ")

    #returning customer input as a list
    return customerInput.lower().split()

def refill(item,quantities) :

    global refillCount

    if refillCount%3==0:
        for x in cafe.values():
            x['stock'] = x['refill']

    #stock refill checking conditions
    elif (cafe[item]['stock'] <= (cafe[item]['refill'] * 0.2)) or (cafe[item]['stock'] - quantities < 0) :
        cafe[item]['stock'] = cafe[item]['refill']
        print(f"{item} Refilled....")
        refillCount += 1
       
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

                    if quantities > cafe[item]['refill'] :

                        quantities = 0
                        print(f'{item} can"t be provided')
                        break

                    #updating the sales quantity and total profit
                    cafe[item]['sales'] += quantities
                    cafe[item]['stock'] -= quantities
                    cafe[item]['totalProfit'] += cafe[item]['profit']*cafe[item]['sales']

                    #refill checking function
                    refill(item,quantities)

                    #displaying the price of the items buyed
                    if quantities != 0 :

                        print(f'{item.capitalize()} Cost = {cafe[item]["price"] * quantities}')

                    #calculating the total bill to be paid
                    totalCost += (cafe[item]['price'] * quantities)
                    list1[i] = 'a'
                    break      
                  
    print(f'Total bill = {totalCost}')


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

    for z in cafe.values() :
        if z['category'] == 'hot' :
            z['stock'] = z['refill']

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
        if z['category'] == 'cold' :
            z['stock'] = z['refill']

main()