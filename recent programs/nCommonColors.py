noOfFriends = int(input("Enter number of friends : "))
print("\t\t------")
friendsColor = {}

def getColor(i):

    colorList = []

    while (True) :
        color = input(f"Friend {i+1}, What color you like? n to exit : " )

        if color=='n' :
            print("\t\t------")
            break

        colorList.append(color)

    return colorList
    

def commonColor(commonColors,i):

    commonColor = []

    for y in friendsColor['friend' + str(i)]:

        if y in commonColors:
            commonColor.append(y)

    return commonColor

for i in range(noOfFriends):

    friendsColor.update({'friend' + str(i) : getColor(i)})

    if i == 0 :
        commonColors = friendsColor['friend'+str(i)]
        
    commonColors = commonColor(commonColors,i)

print(f'Common Colors for all Friends are : {commonColors}')