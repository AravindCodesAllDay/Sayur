#Fill in the missing code whereever it says #FillinMissingCode
#Fix the syntax errors as needed.

#This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
#add new functions as needed.

#The main functions is to find the total profit

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

def avgSales(itemSales):
    totalSales = 0
    for sale in itemSales:
        totalSales = addTwoNumbers(totalSales,sale)
    return divideAFromB(len(itemSales),totalSales)

#main code
def main ():
    #we have sales data for a week. 
    costOfCoffee, costOfTea, costOfVadai = 25,20,25

    coffeeSales = [56,78,56,45,90, 103,120]
    teaSales = [100,123,456,123,222,400,346]
    vadaiSales = [23,45,67,12,89,90,120]

    #Find total sales in the week.
    avgCoffee = avgSales(coffeeSales)
    avgTea = avgSales(teaSales)
    avgVadau = avgSales(vadaiSales)
    #calculate avg sales for a week
    print(f"Average sale for coffee in a week is {avgCoffee}")  
    print(f"Average sale for tea in a week is {avgTea}")  
    print(f"Average sale for vadai in a week is {avgVadau}")         

    employeeSalary = 500 #Rs500 per day

    #calcuate sales per month
    print(f"Average sale for coffee in a week is {avgCoffee*4}")  
    print(f"Average sale for tea in a week is {avgTea*4}")  
    print(f"Average sale for vadai in a week is {avgSales(vadaiSales)*4}")

    #calculate profit.


    #Call divide function to get the average from all three subjects
    #FillinMissingCode
   
main()