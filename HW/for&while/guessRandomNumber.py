######## Problem 2 ###############
# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly 
# https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number

import random#FillinMissingCode
computerNo = random.randint(3, 9)
attempt = 0
while(True):
    userNo = int(input("Enter ur guess : "))
    #FillinMissingCode
    attempt +=1
    if userNo == computerNo:
        print(f"u found the number {computerNo} in attempt {attempt}")
        break
    elif userNo > computerNo:
        print('Lower')
        continue
    print('Higher')

#output:
'''
Enter ur guess : 5
Higher
Enter ur guess : 7
u found the number 7 in attempt 2
'''