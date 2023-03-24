movieSales = {
    'avatar' : {
        'price' : 50,
        'profit' : 14,
        'stock' : 20,
        'sales' : 0,
        'refill' : 20
    },
    'johnWick' : {
        'price' : 35,
        'profit' : 10,
        'stock' : 30,
        'sales' : 0,
        'refill' : 30
    },
    'ironMan' : {
        'price' : 30,
        'profit' : 5,
        'stock' : 40,
        'sales' : 0,
        'refill' : 40
    }
}

a = sorted(movieSales.items(),key = lambda x:x[1]['stock'],reverse=True)[:3]

print(a)
