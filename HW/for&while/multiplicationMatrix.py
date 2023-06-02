######## Problem  4  ###############

#print a multiplication table like below.
#get user intput for start and end numbers. 
#the following example uses 1 to 5.
"""
     1  2  3  4  5
  ********************
1 |  1  2  3  4  5
2 |  2  4  6  8 10
3 |  3  6  9 12 15
4 |  4  8 12 16 20
5 |  5 10 15 20 25
"""

start= int(input("Enter a start value : "))
end =int(input("Enter a end value : "))
a = ' '
b = ' '
for i in range(start,end+1):
    a+= '\t' +str(i)
    b+='__'
print(a)
print(b)
for i in range(start,end+1):
    a =str(i)+' |   '
    for j in range(start,end+1):
        a+=str(i*j)+'\t'
    print(a)

#output:
'''
Enter a start value : 12
Enter a end value : 18
        12      13      14      15      16      17      18
 ______________
12 |   144      156     168     180     192     204     216
13 |   156      169     182     195     208     221     234
14 |   168      182     196     210     224     238     252
15 |   180      195     210     225     240     255     270
16 |   192      208     224     240     256     272     288
17 |   204      221     238     255     272     289     306
18 |   216      234     252     270     288     306     324
'''
