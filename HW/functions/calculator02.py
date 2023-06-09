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

def avgCalculator(subject):
    total = 0
    for mark in subject:
        total = addTwoNumbers(total,mark)

    return divideAFromB(len(subject),total)
    
#main code 
mathsTotal = 0
scienceTotal = 0
historyTotal = 0

#FillinMissingCode to calculate avg for Maths
marksInMaths = [56,78,56,45,90]
marksInScience = [90,78,67,8,98]
marksInHistory = [87,44,56,34,90]

#Call divide function to get the average from all three subjects
#FillinMissingCode
mathsAvg = avgCalculator(marksInMaths)
scienceAvg = avgCalculator(marksInScience)
historyAvg = avgCalculator(marksInHistory)

print("The avg mark is ", mathsAvg)
print("The avg mark is ", scienceAvg)
print("The avg mark is ", historyAvg)

#output:
'''
The avg mark is  65.0
The avg mark is  68.2
The avg mark is  62.2
'''