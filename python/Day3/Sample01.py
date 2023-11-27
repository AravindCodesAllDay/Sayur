# Problem 1
# Print the following pattern
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1

# Observe how the nunmbers in the triangle are calculated. 
# Do it in two steps. Work on the generating the numbers first in right angle triangle
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

# And then work on the final output using proper indendation

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
