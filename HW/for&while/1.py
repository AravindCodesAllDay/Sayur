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
'''
n = 5
pattern = [[0] * ((2*n)-1) for i in range((2*n-1))]
for i in range(0,(n*2)-1,-1):
    for j in range(0,(2*n)-i,-1):
        pass

for row in pattern:
    string = ''
    for num in row:
        string += str(num)
    print(string)


'''
def print_pattern(n):
    for i in range(n, 0, -1):
        for j in range(n, i-1, -1):
            print(j, end=' ')
        for k in range(i+1, n+1):
            print(k, end=' ')
        print()
    
    for i in range(1, n):
        for j in range(n, i, -1):
            print(j, end=' ')
        for k in range(i+1, n+1):
            print(k, end=' ')
        print()

n = 5
print_pattern(n)



