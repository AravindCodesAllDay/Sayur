############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the color"
#Continue until they is atleast 3 movies they both like

#init variables
movieslist=[]
movieslist2=[]
print("Friend 1")
while (True) :
    movies = input(f"What movie you like? n to exit : " )
    if movies=='n' :
        break
    #convert movies into a List
    movieslist.append(movies)
    #FillinMissingCode
print("Friend 2")
print("Get atleast 3 common movies")
commonMovieCount = 0
while (True) :
    #ask the second friend for one movie at a time
    movie = input("Enter a movie you like : " )#FillinMissingCode
    #Check if this movie is in the movie list
    if movie in movieslist:
        #FillinMissingCode
        #if present, 
        commonMovieCount += 1
        movieslist2.append(movie)
     
    #check if we reached the max
    if(commonMovieCount >= 3):
        break;
    else:
        print (f"common count = {commonMovieCount} ")

print (f'common movies = {movieslist2}') #FillinMissingCode - list all the common movies

#output:
'''
Friend 1
What movie you like? n to exit : josee
What movie you like? n to exit : your name
What movie you like? n to exit : silent voice
What movie you like? n to exit : owl's moving castle
What movie you like? n to exit : sprited away
What movie you like? n to exit : n
Friend 2
Get atleast 3 common movies
Enter a movie you like : sprited away
common count = 1
Enter a movie you like : dororo
common count = 1
Enter a movie you like : silent voice
common count = 2
Enter a movie you like : children of the sea
common count = 2
Enter a movie you like : your name
common movies = ['sprited away', 'silent voice', 'your name']
'''

############## Problem  2 #################### 
#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.

monthlySalesList = [5,23,21,14,23,12,4,12,22,22,34,12]  # Sample number of phones sold in each month in a year
#FillinMissingCode - initialise all the variables needed

for month, phoneCount in enumerate(monthlySalesList):
    #calculate the Salary using If stmts
    currentMonthlySalary = 10000
    #FillinMissingCode
    if phoneCount>5:
        currentMonthlySalary += (phoneCount*1100)
    currentMonthlySalary += (5000*int(phoneCount/5))   
    if currentMonthlySalary>20000:
        currentMonthlySalary=20000     
    
    print (f"month {month+1} salary before additional bonus {currentMonthlySalary}") 

    #check for condition #If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
    # this month also, then he gets additional Rs5000.

    if(phoneCount < 20):
        previousMonthSalary = currentMonthlySalary #we set this so that, we can use this info in the next iteration
        continue #no need to calculate anything because <20 phones sold
    
    #calculate the new salary
    currentMonthlySalary += 5000   #FillinMissingCode
    print(f'month {month+1} salary after additional bonus {currentMonthlySalary}')
    previousMonthSalary = currentMonthlySalary #Why are we doing this?

#output:
'''
month 1 salary before additional bonus 15000
month 2 salary before additional bonus 20000
month 2 salary after additional bonus 25000
month 3 salary before additional bonus 20000
month 3 salary after additional bonus 25000
month 4 salary before additional bonus 20000
month 5 salary before additional bonus 20000
month 5 salary after additional bonus 25000
month 6 salary before additional bonus 20000
month 7 salary before additional bonus 10000
month 8 salary before additional bonus 20000
month 9 salary before additional bonus 20000
month 9 salary after additional bonus 25000
month 10 salary before additional bonus 20000
month 10 salary after additional bonus 25000
month 11 salary before additional bonus 20000
month 11 salary after additional bonus 25000
month 12 salary before additional bonus 20000
'''
