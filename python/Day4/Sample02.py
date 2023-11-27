# Problem #2
# You have 6 x 6 game board where each cell is shown as a *
# This is a two player dice game. The die has numbers 1 to 6.
# Each player rolls the dice twice. First roll is row number, second roll is col number.
# After the player rolls the dice, in the (row,col) enter the player's initial. 
# If the player  A rolls the dice and  if  player B already has their initial in the same row,col
# add a point to A and change the initial to A. 

# Player who gets 5 points first wins the game.
# Print the board each time after the user rolls and also print the current score.
# Use functions

import random

board = {
    1 : ['*'] * 6,
    2 : ['*'] * 6,
    3 : ['*'] * 6,
    4 : ['*'] * 6,
    5 : ['*'] * 6,
    6 : ['*'] * 6
}

def roll(initial):
    score = 0
    rowDice = random.randrange(1,6)
    colDice = random.randrange(1,6)

    print(f'you rolled : ({rowDice},{colDice})')

    if (board[rowDice][colDice-1] != '*' and board[rowDice][colDice-1] != initial):
        board[rowDice][colDice-1] = initial
        score = 1
        return score
    
    board[rowDice][colDice-1] = initial
    return score

def printBoard():
    cols = ''

    for row in board.keys():

        for col in board[row]:
            cols += col + ' '

        print(cols)
        cols = ''


def main():   

    aScore = 0
    bScore = 0
    round = 1

    while(aScore<5 and bScore<5):

        print(f'Round-{round}')
        printBoard()
        print(f'A scored : {aScore}')
        print(f'B scored : {bScore}')

        if round%2 == 1:
            a = input("Player A press enter to roll")
            aScore += roll('a')
        else:
            b = input("Player B press enter to roll")
            bScore += roll('b')

        round += 1

    if aScore==5:
        print('A wins')
    else:
        print('B wins')

main()
