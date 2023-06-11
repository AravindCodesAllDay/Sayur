'''
Program 1 - Write a program to print the following pattern.
Input is 5 for the following pattern.
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
'''

n = int(input("Enter outer layer number : "))
a  = [''for i in range((2*n)-1)]

for i in range(1,n+1):
    b = n
      
    for j in range(1,n+1):
        a[n-i]+=str(b)
        if j <= n-i:
            b = n-j
        if j == n :
            a[n-i] +=  a[n-i][:n-1][::-1]    
    
for i in range(n-1):
    a[-1-i] = a[i]
    
for i in a:
    print(i)
