'''
Get the list of employee names from the user.
Get the monthly phone sales for each employee for the first 4 months of the year.
Sort the employees by name in alphabetical order and for each employee sort their phones sales in 
ascending order.

Eg - Sam, Adam, Sara
Sam's sales - 300, 567,234,1000
Adam's Sales - 340, 456,456,234
Sara' Sales - 1000,234,3000,2000

Output sample
Adam - 456,456,340,234
Sam - ...
Sara - ...

'''


def seperateNames():

    employeeData = {}
    employeeNames = input("Enter employee names : ").split(",")

    for name in employeeNames:
        sales = []

        for month in range(1, 5):
            sale = int(input(f"Enter phone sales for {name} in month {month}: "))
            sales.append(sale)

        employeeData[name] = sales
    return employeeData

employeeData = seperateNames()

def seperateEmployeeData(employeeData):

    sorted_names = sorted(employeeData.keys())
    
    for name in sorted_names:
        sortedSales = sorted(employeeData[name])
        salesString = ", ".join(str(sale) for sale in sortedSales)
        print(f"{name} - {salesString}")

seperateEmployeeData(employeeData)
