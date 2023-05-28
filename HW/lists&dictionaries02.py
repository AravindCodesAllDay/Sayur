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
    color = input(f"What movie you like? n to exit : " )
    if color=='n' :
        break
    #convert movies into a List
    colorList1.append(color)
    #FillinMissingCode

while (True) :
    #ask the second friend for one movie at a time
    color = input("Enter a movie you like, n to exit : " )#FillinMissingCode
    if color=='n' :
        break
    #Check if this movie is in the movie list
    if color in colorList1:
        #FillinMissingCode
        #if present,       
        colorList2.append(color)
        continue
    colorList3.append(color)
print(f'colors liked by 1st friend {colorList1}')
print(f'colors liked by 2nd friend {colorList3}')
print(f'colors liked by both friends {colorList2}')

print (f'common colors = {colorList2}') #FillinMissingCode - list all the common movies

############## Problem 2 ####################
#Ask the user how many members in the family. Get Name, age and height and weight.
#add the details into four lists.
#Print the each memeber of the family and their details
#eg output 
# Name      Age     Height(cm)      Weight(kg)
# Ram       35      180             80
# Seetha    34      145             58
#
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
