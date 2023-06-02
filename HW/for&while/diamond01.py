######## Problem 3  ###############
#Write a program that prints out a diamond shape using #.
# Hint - print(5 * "$") will print  - $$$$$
# Hint - print(5* "$ ") will print  - $ $ $ $ $

n = int(input("Enter the number of rows: "))
#print the top triangle
for i in range(n):
    print(" "*(n - i) + "$"*(2*i-1))
#FillinMissingCode for drawing the bottom triangle
for i in range(n - 1, 0, -1):
    print(" "*(n - i) + "$"*(2*i-1))
    
#output:
'''
Enter the number of Characters : 3 
  $ 
 $$$ 
 $$$ 
  $
'''

