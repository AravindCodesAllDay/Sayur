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
    print(f"your BMI is {bmi} and ur Under weight")
elif bmi <24.9 :
    print(f"your BMI is {bmi} and ur in Healthy weight range")
elif bmi<29.9 :
    print(f"your BMI is {bmi} and ur Over weight")
else :
    print(f"your BMI is {bmi} and ur Obese")

#output:
'''
enter ur weight in kg : 48
enter ur height in meters : 1.61
your BMI is 18.4 and ur Under weight
'''