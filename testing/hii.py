itemsInCafe = ['coffee','tea','cappucino','cookie']
itemPrice = [40,35,50,30]
itemProfit = [12,10,14,5]
itemStock = [30,30,20,40]
itemStockRefill = [30,30,20,40]
itemSales = [0,0,0,0]
topSale = [0,0,0,0]
topProfit = [0,0,0,0]


cafe = {
    'coffee' : {
        'price' : 40,
        'profit' : 12,
        'stock' : 30,
        'sales' : 0
    },
    'tea' : {
        'price' : 35,
        'profit' : 10,
        'stock' : 30,
        'sales' : 0
    },
    'cappucino' : {
        'price' : 50,
        'profit' : 14,
        'stock' : 20,
        'sales' : 0
    },
    'cookie' : {
        'price' : 30,
        'profit' : 5,
        'stock' : 40,
        'sales' : 0
    }
}

for x in cafe.items():
    print(x)





