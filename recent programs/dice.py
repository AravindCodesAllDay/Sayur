'''
1. Write an app for the follwoing two player game. You have a 6 x 6 board. 
Users take turns rolling the dice twice. first roll is row no, second roll is col number. 
Mark the spot (row, col) as claimed by the user who rolled the dice.
When the user rolls the dice within 1 col/row of a claimed spot of the other user, the other user gets a point. 
If the spot is same as the claimed spot of the other user, the user that rolled the dice gets a point. 
The player who gets 5 points first wins the game.
'''

#PROGRAM :

import random

player1 = {
    'points' : 0,
    'ownedBox' : [[0,0]]
}

player2 = {
    'points' : 0,
    'ownedBox' : [[0,0]]
}

def Player1(diceValue) :

    print(f'Player1 rolls {diceValue}')

    for x,y in player2['ownedBox'] :

        if [x,y] == diceValue :

            player1['points'] += 1
            break

        elif [x-1,y] == diceValue or [x+1,y] == diceValue or [x,y-1] == diceValue or [x,y+1] == diceValue :

            player2['points'] += 1
            break
        
    if diceValue not in player1['ownedBox'] and diceValue not in player2['ownedBox'] :
        player1['ownedBox'].append(diceValue)

    
def Player2(diceValue) :

    print(f'Person2 rolls {diceValue}')

    for x,y in player1['ownedBox'] :

        if [x,y] == diceValue :

            player2['points'] += 1
            break
        
        elif [x-1,y] == diceValue or [x+1,y] == diceValue or [x,y-1] == diceValue or [x,y+1] == diceValue :

            player1['points'] += 1
            break
        
    if diceValue not in player2['ownedBox'] and diceValue not in player2['ownedBox'] :

        player2['ownedBox'].append(diceValue)

def display():

    print(f'Player 1 score = {player1["points"]}')
    print(f'Player 2 score = {player2["points"]}\n')

def main():

    rollCount = 0

    while player1['points'] < 5 or player2['points'] < 5 :

        a = input('roll...  ')
        diceValue = [random.randint(1,6),random.randint(1,6)]

        if rollCount%2 == 0 :
            Player1(diceValue)

        else :
            Player2(diceValue)

        display()

        rollCount += 1

main()





