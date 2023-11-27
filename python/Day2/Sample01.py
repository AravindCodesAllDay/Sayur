# Problem #1
# Print the following pattern
# 1
# 212
# 32123
# 4321234
# 543212345
# Get user input for how far to go (up to 0)


customNum = int(input("Enter a number 1-9 : "))

if(customNum>=0  and customNum<=9):

    x=1
    finalString = ''

    while(x<=customNum):
        if (x!=1):
            finalString += str(x)
        finalString = str(x) + finalString
        print(f'{" " * (customNum-x)}{finalString}')
        x += 1

else:
    print("error enter a value between 1-9")

