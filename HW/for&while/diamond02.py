######## Problem 1 ###############
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines

n = int(input("Enter the number of Characters : "))
#print the top triangle
for i in range(n):
    a =input()
    if a!=' ':
        break
    print(" "*(n - i) + "$"*(2*i-1))

for i in range(n - 1, 0, -1):
    if a != ' ' :
        break
    a=input()
    print(" "*(n - i) + "$"*(2*i-1))
    
#Output:
'''
Enter the number of Characters : 3

 
  $
 
 $$$
 
 $$$
 
  $
'''