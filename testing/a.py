
itemsInCafe = ['coffee','tea','cappucino','cookie']
itemPrice = [40,35,50,30]
itemProfit = [12,10,14,5]
itemStock = [30,30,20,40]
itemStockRefill = [30,30,20,40]
itemSales = [10,30,40,20]
topSale = [0,0,0,0]
topProfit = [0,0,0,0]

for x in range(len(itemSales)) :
    topProfit[x] = itemSales[x] * itemProfit[x]
    
itemsInCafeList = list(enumerate(itemsInCafe))
topSale = list(enumerate(itemSales))
topProfit = list(enumerate(topProfit))
print(itemsInCafeList)
print(topSale)
print(topProfit)

sortTopSale = sorted(topSale,key = lambda x:x[1],reverse=True)
sortTopProfit = sorted(topProfit,key = lambda x:x[1],reverse=True)

for i in sortTopSale[0:3]:
    print(f'{itemsInCafeList[i[0]]}')
for y in sortTopProfit[0:3]:
    print(f'{itemsInCafeList[y[0]]}')
