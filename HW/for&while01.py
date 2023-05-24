#write code for both for and while loop
#Get marks from 5  students and calculate avg
#

#for loop
total = 0
studentCount = 5
for i in range(studentCount):#FillinMissingCode
    #get user input
    mark = int(input(f"Enter mark for student {i+1} : "))
    #FillinMissingCode
    total += mark
print("Avg is : ",total/studentCount )#FillinMissingCode

#using while loop
total = 0
noOfStudents = 5
i = 0
while (i < noOfStudents):
    #get user input
    mark = int(input(f"Enter mark for student {i+1} : "))
    #FillinMissingCode
    total += mark
    i += 1
print ("Avg is : ", total/noOfStudents)  #FillinMissingCode