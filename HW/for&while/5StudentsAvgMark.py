#write code for both for and while loop
#Get marks from 5  students and calculate avg
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

#output:
'''
Enter mark for student 1 : 60
Enter mark for student 2 : 40
Enter mark for student 3 : 70
Enter mark for student 4 : 50
Enter mark for student 5 : 35
Avg is :  51.0
'''