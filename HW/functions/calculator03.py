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

def total(itemSales):
    totalSales = 0
    for sale in itemSales:
        totalSales = addTwoNumbers(totalSales,sale)
    return totalSales

#main code
def main ():
    #we have sales data for a week. 
    costOfCoffee, costOfTea, costOfVadai = 25,20,25

    coffeeSales = [56,78,56,45,90, 103,120]
    teaSales = [100,123,456,123,222,400,346]
    vadaiSales = [23,45,67,12,89,90,120]
   
    #Call divide function to get the average from all three subjects
    totalCoffee = total(coffeeSales)
    totalTea = total(teaSales)
    totalVadau = total(vadaiSales)

    #Find total sales in the week.
    print(f"Total sale for coffee in a week is {totalCoffee}")  
    print(f"Total sale for tea in a week is {totalTea}")  
    print(f"Total sale for vadai in a week is {totalVadau}")   

    #calculate avg sales for a week
    print("\t\t-------------")
    print(f"Average sale for coffee in a week is {divideAFromB(totalCoffee,len(coffeeSales))}")  
    print(f"Average sale for tea in a week is {divideAFromB(totalTea,len(teaSales))}")  
    print(f"Average sale for vadai in a week is {divideAFromB(totalVadau,len(vadaiSales))}")         

    employeeSalary = 500 #Rs500 per day

    #calcuate sales per month
    print("\t\t-------------")
    print(f"Average sale for coffee for a month is {divideAFromB(totalCoffee,len(coffeeSales))*4}")  
    print(f"Average sale for tea for a month is {divideAFromB(totalTea,len(teaSales))*4}")  
    print(f"Average sale for vadai for a month is {divideAFromB(totalVadau,len(vadaiSales))*4}")

    #calculate profit.
    print("\t\t-------------")
    print(f"Total Profit for coffee in a week is {multiplyTwoNumbers(totalCoffee,costOfCoffee)}")  
    print(f"Total Profit for tea in a week is {multiplyTwoNumbers(totalTea,costOfTea)}")  
    print(f"Total Profit for vadai in a week is {multiplyTwoNumbers(totalVadau,costOfVadai)}")     
    #FillinMissingCode
   
main()