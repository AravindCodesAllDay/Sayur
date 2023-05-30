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

#main code
 
mathsTotal = 0
scienceTotal = 0
historyTotal = 0

marksInMaths = [56,78,56,45,90]
#FillinMissingCode to calculate avg for Maths
for i in marksInMaths:
    mathsTotal = addTwoNumbers(mathsTotal,i)

marksInScience = [90,78,67,8,98]
#FillinMissingCode to calculate avg for Science
for i in marksInScience:
    scienceTotal = addTwoNumbers(scienceTotal,i)

marksInHistory = [87,44,56,34,90]
#FillinMissingCode to calculate avg for History
for i in marksInHistory:
    historyTotal = addTwoNumbers(historyTotal,i)

#Call divide function to get the average from all three subjects
#FillinMissingCode
mathsAvg = divideAFromB(len(marksInMaths),mathsTotal)
scienceAvg = divideAFromB(len(marksInScience),scienceTotal)
historyAvg = divideAFromB(len(marksInHistory),historyTotal)

print("The avg mark is ", mathsAvg)
print("The avg mark is ", scienceAvg)
print("The avg mark is ", historyAvg)

#output:
'''
The avg mark is  65.0
The avg mark is  68.2
The avg mark is  62.2
'''