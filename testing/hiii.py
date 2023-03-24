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

cusInput = '1 coffee 2 tea cookie 3 4 cappucino'

cusInput = cusInput.split()

for x in cusInput:
    
    if x in cafe.keys():

        for y in cusInput:

            if y.isnumeric():

                cafe[x]['sales'] += int(y)
                cafe[x]['stock'] -= int(y)
                a = cusInput.index(y)
                cusInput[a] = 'a'
                break

print(cafe)








