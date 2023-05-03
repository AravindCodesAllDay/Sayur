'''
A program to keep count of the points scored in a bowling game
'''

#PROGRAM :

import random

def rolls() :

    #to give empty space
    roll = input('Roll..')
    #getting frame values using random
    a = random.randint(0,10)
    n = 10 - a
    b = random.randint(0,n)

    print(f'[{a},{b}]')

    #returning as a 2d list
    return [a,b]

def points(values) :

    score = 0

    for i in range(10) :
        
        #checking to adding values
        #for strike
        if values[i][0] == 10 :
            score += values[i][0] + values[i+1][0] + values[i+1][1]
        #for spare
        elif values[i][0] + values[i][1] == 10 :
            score += values[i][0] + values[i][1] + values[i+1][0]
        
        else :
            score += values[i][0] + values[i][1]
            
    return score

def main() :

    values = []

    #for n number of frames
    for i in range(11) :

        print(f'\nset-{i+1}')

        values.append(rolls())
                  
    print(values)

    totalScore = points(values)

    print(totalScore)
    
main()