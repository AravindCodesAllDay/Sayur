############## Problem 4 ##############
#Calculate the Grade for a student, using 3 marks.
# The student has 100 marks in any one subject, Grade is A.
# if the student has 90 or above in any one subject  Grade is B
# if the student has 60 or above in any one subject  Grade is C
# if the student has 50 or less  in all subjects  Grade is F, otherwise Grade is D.

#Code
mark1 = int(input("enter ur mark in sub 1 : ")) #FillinMissingCode
mark2 = int(input("enter ur mark in sub 2 : "))#FillinMissingCode
mark3 = int(input("enter ur mark in sub 3 : "))#FillinMissingCode

if(mark1 == 100 or mark2 == 100 or mark3 == 100): #at leasr one mark is 100
    print("Grade A")
elif mark1>89 or mark2>89 or mark3>89 :#FillinMissingCode 
    print("Grade B")
elif mark1>59 or mark2>59 or mark3>59 :#FillinMissingCode
    print("Garde C")
elif mark1<50 or mark2<50 or mark3<50 :#FillinMissingCode
    print ("Grade D")
else :
    print ("Grade F")

#output:
'''
enter ur mark in sub 1 : 90
enter ur mark in sub 2 : 40
enter ur mark in sub 3 : 80
Grade B
'''