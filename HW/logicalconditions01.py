############# Problem 1 ###########
#Google and find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary. Optional input - any deductions.

"""₹ 3,00,000                      No Tax

₹ 3,00,001 to ₹ 6,00,000           5%

₹ 6,00,001 to ₹ 9,00,000           10%

₹ 9,00,001 to ₹ 12,00,000          15%

₹ 12,00,001 to ₹ 15,00,000         20%

>₹ 15,00,000                       30%"""

income = int(input("enter your monthly salary : "))
taxDeduction = int(input('Enter tax detuction in percentage,if any : '))

if income<300001:
    print(f"your actual salary after tax is {income}")
elif income<600001:
    print(f"your actual salary after tax is {income*(0.95-(taxDeduction/100))}")
elif income<900001:
    print(f"your actual salary after tax is {income*(0.90-(taxDeduction/100))}")
elif income<1200001:
    print(f"your actual salary after tax is {income*(0.85-(taxDeduction/100))}")
elif income<1500001:
    print(f"your actual salary after tax is {income*(0.80-(taxDeduction/100))}")
else:
    print(f"your actual salary after tax is {income*(0.70-(taxDeduction/100))}")

############ Problem 2 ####
#Calculate the BMI and if the person is underweihgt/normal/overweight/obese
#Google how to calculate BMI and decide on the input.
#If your BMI is less than 18.5, it falls within the underweight range. 
# If your BMI is 18.5 to 24.9, it falls within the Healthy Weight range. 
# If your BMI is 25.0 to 29.9, it falls within the overweight range
#If your BMI is 30.0 or higher, it falls within the obese range.

weight = float(input("enter ur weight in kg : "))
height = float(input("enter ur height in meters : "))
bmi = weight/(height**2)
if bmi <18.5 :
    print(f"your BMI is  {bmi} and ur Under weight")
elif bmi <24.9 :
    print(f"your BMI is  {bmi} and ur in Healthy weight range")
elif bmi<29.9 :
    print(f"your BMI is  {bmi} and ur Over weight")
else :
    print(f"your BMI is  {bmi} and ur Obese")

########## Problem 3 ##########
##buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user. Also get the total number of choc and cakes that the shop has
#Hint - you can buy choc/Cake only if shop has it.

cusBudget = int(input("Enter ur Budget to buy In Bakery : "))
chocCount = int(input("enter the number of chocolate available in shop : "))
cakeCount = int(input("enter the number of cake available in shop : "))
#find how many choc and cake the user can buy.
chocoBought  = int(cusBudget/200)
cakeBought = int(cusBudget/150)
if chocCount<cakeBought :
    chocoBought=chocCount
if cakeCount<cakeBought :
    cakeBought=cakeCount
print(f"The total number of chocolate or cake you can buy is {chocoBought} and {cakeBought}")

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
elif mark1<89 or mark2<89 or mark3<89 :#FillinMissingCode 
    print("Grade B")
elif mark1<59 or mark2<59 or mark3<59 :#FillinMissingCode
    print("Garde C")
elif mark1<50 or mark2<50 or mark3<50 :#FillinMissingCode
    print ("Grade D")
else :
    print ("Grade F")