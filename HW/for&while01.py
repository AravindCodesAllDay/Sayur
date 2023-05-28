#write code for both for and while loop
#Get marks from 5  students and calculate avg
#

#for loop
total = 0
studentCount = 5
for stdRoll in range(1,studentCount+1):#FillinMissingCode
    #get user input
    mark = int(input(f"Enter mark for student {stdRoll} : "))
    #FillinMissingCode
    total += mark
print("Avg is : ",total/studentCount )#FillinMissingCode

#using while loop
total = 0
noOfStudents = 5
stdRoll = 1
while (stdRoll <= noOfStudents):
    #get user input
    mark = int(input(f"Enter mark for student {stdRoll} : "))
    #FillinMissingCode
    total += mark
    stdRoll += 1
print ("Avg is : ", total/noOfStudents)  #FillinMissingCode
