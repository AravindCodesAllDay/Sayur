#Fill in the missing code whereever it says #FillinMissingCode
#Fix the syntax errors as needed.

#This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
#The main function adds all student marks and finds the average

def addTwoNumbers(n1, n2):
    ans = n1 + n2
    return ans

def subtractAfromB(a, b):
    ans = b-a#FillinMissingCode
    return ans #FillinMissingCode

def multiplyTwoNumbers(n1,n2):
    ans = n1 * n2#FillinMissingCode
    return #FillinMissingCode

def divideAFromB(a, b):
    ans = b / a
    return ans #FillinMissingCode

#main codeiu

#Get 5 marks from student and find the total
total = 0
for i in range(1,6):
    mark = (int(input(f"Enter mark of sub {i} : "))) #correct te syntax as needed
    total = addTwoNumbers(total,mark) #FillinMissingCode

#Call divide function to get the average
avgMark= divideAFromB(5,total)
#FillinMissingCode

print("The avg mark is ", avgMark)

#output:
'''
Enter mark of sub 1 : 60
Enter mark of sub 2 : 40
Enter mark of sub 3 : 50
Enter mark of sub 4 : 70
Enter mark of sub 5 : 30
The avg mark is  50.0
'''