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

print (f'common colors = {colorList2}') 

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

############## Problem 2 ####################
#Ask the user how many members in the family. Get Name, age and height and weight.
#add the details into four lists.
#Print the each memeber of the family and their details
#eg output 
# Name      Age     Height(cm)      Weight(kg)
# Ram       35      180             80
# Seetha    34      145             58

nameList = []
ageList = []
heightList = []
weightList = []
#FillinMissingCode for other data
noOfPeople = int (input("How many people in the family : "))

for member in range (1, noOfPeople + 1):

    details = input(f"Enter the details of member {member} Name, age, height, weight : ")
    #FillinMissingCode Split the input string and add it to the lists
    details = details.split()
    nameList.append(details[0])
    ageList.append(details[1])
    heightList.append(details[2])
    weightList.append(details[3])                  
    
#print the header 
print ("Name\t\tAge\t\tHeight(cm)\t\tWeight(kg)") #learn about \t
for index, member in enumerate(nameList): #Learn how enumerate works
    print( f"{member}\t\t {ageList[index]}\t\t{heightList[index]}\t\t{weightList[index]}")   

#output:
'''
How many people in the family : 2          
Enter the details of member 1 Name, age, height, weight : tom 19 161 48
Enter the details of member 2 Name, age, height, weight : jerry 14 120 28
Name            Age             Height(cm)              Weight(kg)
tom              19             161             48
jerry            14             120             28
'''     
