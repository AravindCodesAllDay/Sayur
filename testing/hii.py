from collections import Counter


cafe = {
    'coffee' : {
        'price' : 40,
        'profit' : 12,
        'stock' : 30,
        'sales' : 6
    },
    'tea' : {
        'price' : 35,
        'profit' : 10,
        'stock' : 30,
        'sales' : 3
    },
    'cappucino' : {
        'price' : 50,
        'profit' : 14,
        'stock' : 20,
        'sales' : 4
    },
    'cookie' : {
        'price' : 30,
        'profit' : 5,
        'stock' : 40,
        'sales' : 2
    }
}

'''
my_keys = sorted(cafe,key=cafe.get() , reverse=True)

print(my_keys)

    t3Sales = sorted(topSales,key = topSales() ,reverse=True)


c = Counter(cafe['cappucino'])

most_common = c.most_common(1)

print(most_common)
'''

topSales = {
    'coffee' : cafe['coffee']['sales'],
    'tea' : cafe['tea']['sales'],
    'cappucino': cafe['cappucino']['sales'],
    'cookie': cafe['cookie']['sales']
}



sorted_dict = (sorted(topSales.items(),key=lambda x:x[1],reverse=True)[:3])
print(sorted_dict)
'''
print(topSales)

from collections import OrderedDict

# Sorting dictionary
 
# Printing sorted dictionary
print(sorted_dict)



my_keys = sorted(topSales.keys(),key=topSales.get() , reverse=True)[:3]

print(my_keys)

'''
