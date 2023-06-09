############## Problem  1 #################### 
#Ask first friend the colors they like. Save it in a list
#Ask another friend the same question. If the color is in the first friend's list, 
#Print "You both like "name of the color"
#If it is not in the first friend's list, Save it another list.

#init variables
colorList1=[]
colorList2=[]
colorList3=[]
while (True) :
    color = input(f"What color you like? n to exit : " )
    if color=='n' :
        break
    colorList1.append(color)
    #FillinMissingCode

while (True) :

    color = input("Enter a color you like, n to exit : " )
    #FillinMissingCode
    if color=='n' :
        break 

    if color in colorList1:
        #FillinMissingCode
        #if present,       
        colorList2.append(color)
        continue
    colorList3.append(color)
print(f'colors liked by 1st friend {colorList1}')
print(f'colors liked by 2nd friend {colorList3}')
print(f'colors liked by both friends {colorList2}')


#output:
'''
What color you like? n to exit : red
What color you like? n to exit : blue
What color you like? n to exit : yellow
What color you like? n to exit : orange
What color you like? n to exit : n
Enter a color you like, n to exit : purple
Enter a color you like, n to exit : red
Enter a color you like, n to exit : yellow
Enter a color you like, n to exit : pink
Enter a color you like, n to exit : green
Enter a color you like, n to exit : n
colors liked by 1st friend ['red', 'blue', 'yellow', 'orange']
colors liked by 2nd friend ['purple', 'pink', 'green']
colors liked by both friends ['red', 'yellow']
common colors = ['red', 'yellow']
'''