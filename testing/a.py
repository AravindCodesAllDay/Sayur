
itemsInCafe = ['coffee','tea','cappucino','cookie']

itemsInCafeList = list(enumerate(itemsInCafe))
itemSales = [12,10,4,8]
topSale = list(enumerate(itemSales))
sortTopSale = sorted(topSale,key = lambda x:x[1],reverse=True)
for i,a in enumerate(sortTopSale[0:3]):
    print(f'{i}-{itemsInCafeList[a[0]][1]}-{a[1]}')