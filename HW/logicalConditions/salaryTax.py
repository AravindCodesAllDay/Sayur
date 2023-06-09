############# Problem 1 ###########
#Google and find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary. Optional input - any deductions.

"""
₹ 3,00,000                      No Tax

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

#output:
'''
enter your monthly salary : 400000
Enter tax detuction in percentage,if any : 3 
your actual salary after tax is 392000.0
'''