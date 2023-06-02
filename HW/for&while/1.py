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

n = 5
pattern = [[0] * ((2*n)-1) for i in range((2*n-1))]
for i in range(n):
    for j in range(i, 2*n-i):
        pattern[i][j] = n - i
        pattern[2*n-i-1][j] = n - i
        pattern[j][i] = n - i
        pattern[j][2*n-i-1] = n - i

for row in pattern:
    for num in row:
        print(num, end=' ')
    print()


