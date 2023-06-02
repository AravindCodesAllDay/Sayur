#Write code for drawing these patterns.
#Get width and length from the user.
# draw a empty rectangle woth char *
#eg 
'''
Row 5, col 7
* * * * * * *
*           *
*           *
*           *
* * * * * * *

'''
# next pattern is - empty diamond

width = int(input("enter the width : "))
height = int(input("enter the height : "))
for i in range(height):
    a=''
    for j in range(width):
        if i == 0 or i == height-1 or j==0 or j==width-1:
            a += ' *' 
            continue
        a+='  '
    print(a)

#output:
'''
enter the width : 7
enter the height : 5
 * * * * * * *
 *           *
 *           *
 *           *
 * * * * * * *
'''