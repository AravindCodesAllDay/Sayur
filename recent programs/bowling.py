import random

def rolls() :

    #roll = input('Roll..')
    a = int(input('a'))#random.randint(0,10)
    #n = 10 - a
    b = int(input('b'))#random.randint(0,n)

    print(f'[{a},{b}]')

    return [a,b]

def points(values) :

    score = 0

    for i in range(10) :

        if values[i][0] == 10 :
            score += 2

        elif values[i][0] + values[i][1] == 10 :
            score += 3
        
        else :
            score += values[i][0] + values[i][1]
            
    return score

def main() :

    values = []

    for i in range(11) :

        print(f'set {i+1}')

        values.append(rolls())
                  
    print(values)

    totalScore = points(values)

    print(totalScore)


    
main()