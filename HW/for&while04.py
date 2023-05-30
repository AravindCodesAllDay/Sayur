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

######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number upto 12 rows.

for i in range(7,16+1):
     for j in range(1,12+1):
         print(f"{i}+{j}={i*j}")

######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares

for i in range(8):
    a=''
    for j in range(8):
        if (j+i)%2 == 0:
            a+='b'
            continue
        a+='\u25A0'
    print(a)

#output:
'''
b■b■b■b■
■b■b■b■b
b■b■b■b■
■b■b■b■b
b■b■b■b■
■b■b■b■b
b■b■b■b■
■b■b■b■b
'''

######## Problem  4  ###############

#print a multiplication table like below.
#get user intput for start and end numbers. 
#the following example uses 1 to 5.
"""
     1  2  3  4  5
  ********************
1 |  1  2  3  4  5
2 |  2  4  6  8 10
3 |  3  6  9 12 15
4 |  4  8 12 16 20
5 |  5 10 15 20 25
"""

n= int(input("enter the square matrix n : "))
a = ' '
b = ' '
for i in range(1,n+1):
    a+=str(i)+' '
    b+='__'
print(a)
print(b)
for i in range(1,n+1):
    a =str(i)+' |'
    for j in range(1,n+1):
        a+=str(i*j)+' '
    print(a)

#output:
'''
enter the square matrix n : 3
 1 2 3
 ______
1 |1 2 3
2 |2 4 6
3 |3 6 9
'''
