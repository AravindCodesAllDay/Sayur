############## Problem  2 #################### 
#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and 
#sells 20 or more phones this month also, then he gets additional Rs5000.

monthlySalesList = [5,23,21,14,23,12,4,12,22,22,34,12]  # Sample number of phones sold in each month in a year
#FillinMissingCode - initialise all the variables needed
previousMonthSalary = 0

for month, phoneCount in enumerate(monthlySalesList):
    #calculate the Salary using If stmts
    currentMonthlySalary = 10000
    #FillinMissingCode
    if phoneCount>5:
        currentMonthlySalary += ((phoneCount-5)*1100)
    currentMonthlySalary += (5000*int(phoneCount/5))   
      
    print('\t-----------\t')
    print (f"month {month+1} salary {currentMonthlySalary}") 

    #check for condition #If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
    # this month also, then he gets additional Rs5000.

    if(phoneCount < 20 and previousMonthSalary >20000):
        previousMonthSalary = currentMonthlySalary
        currentMonthlySalary += 5000  
        print(f'month {month+1} salary with additional bonus {currentMonthlySalary}')#we set this so that, we can use this info in the next iteration
        continue #no need to calculate anything because <20 phones sold
    
    #calculate the new salary
    #FillinMissingCode    
    previousMonthSalary = currentMonthlySalary #Why are we doing this?

#output:
'''
        -----------
month 1 salary 15000
        -----------
month 2 salary 49800
        -----------
month 3 salary 47600
        -----------
month 4 salary 29900
month 4 salary with additional bonus 34900
        -----------
month 5 salary 49800
        -----------
month 6 salary 27700
month 6 salary with additional bonus 32700
        -----------
month 7 salary 10000
month 7 salary with additional bonus 15000
        -----------
month 8 salary 27700
        -----------
month 9 salary 48700
        -----------
month 10 salary 48700
        -----------
month 11 salary 71900
        -----------
month 12 salary 27700
month 12 salary with additional bonus 32700
'''