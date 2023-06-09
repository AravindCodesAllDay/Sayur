######## Problem  1 ###############
# Get and print the 2 marks each for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc

######### Problem 1.1
#same problem as above, but output should have the student name and all the marks in the same line.
# Eg - Input - Student Name - Chitra, Mark1 1 55, Mark 2 67
#output -  Chitra's marks 55, 67

numOfStd = 3
numOfMarks = 2
stdList = []
mark1 = []
mark2 = []

for student in range (numOfStd):
    #FillinMissingCode  to get studnet name
    stdList.append(input(f"enter student {student +1} name : "))
    mark1.append(input(f"enter one mark of the student {stdList[student]} : "))
    mark2.append(input(f"enter two mark of the student {stdList[student]} : "))

for i,j in enumerate(stdList):
    print(j,mark1[i],mark2[i])

#output:
'''
enter student 1 name : Tom
enter one mark of the student Tom : 50
enter two mark of the student Tom : 60
enter student 2 name : Jerry
enter one mark of the student Jerry : 30
enter two mark of the student Jerry : 20
enter student 3 name : Terry
enter one mark of the student Terry : 40
enter two mark of the student Terry : 50
Tom 50 60
Jerry 30 20
Terry 40 50
'''
