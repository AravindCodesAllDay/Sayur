# Problem #3
# Its is a single player game where the user starts with 0 points. User keeps rolling the 
# dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
#  added. If the number is odd, then if the number is 1,3 then the user has to jump. 
#  If the number is 5, then 3 points are added. The game ends when the user has 50 points.

import random

score = 0

while(True):
    a = input('Press enter to roll')
    roll = random.randrange(1,6)
    print(f'The rolled number is {roll}')

    if(roll%2 == 0):
        score += 2
        print(f'current score = {score}')

    elif(roll == 1,3):
        print("Jump")
        print(f'current score = {score}')

    else:
        score += 3
        print(f'current score = {score}')

    if (score >= 50):
        break
