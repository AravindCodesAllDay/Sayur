movieSales = {
    'avatar' : 1000,
    'bahubali' : 800,
    'johnWick' : 600,
    'avengers' : 1200,
    'ironMan' : 900
}

#dict(sorted(movieSales.items()))

print(sorted(movieSales.items()))
a = sorted(movieSales.items(),key = lambda x:x[1],reverse=True)[:3]

print(a)
