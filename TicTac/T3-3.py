#!/usr/bin/env python
# Tic-Tac-Toe 1
#    note a comma at the end of the print suppresses the newline

board = [ 'O', 'X', ' ' , 'O', ' ', 'X', 'O', 'X', 'X' ]
wins = [ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6] ]

def printBoard():
    print
    print '|',
    for square in range(0,9):
        print board[square], '|',
        if square == 2 or square == 5 :
            print
            print '- - - - - - -'
            print'|',
    print
    print

def checkWin(player):
    win = False
    for test in wins:
        #print test
        count = 0
        for squares in test:
            if board[squares] == player:
                count +=1
            if count == 3:
                win = True
    return win

if __name__ == '__main__':
    printBoard()
    print 'Checking board for X'
    if checkWin('X'):
        print 'Game Over - X wins'
    print 'Checking board for O'
    if checkWin('O'):
        print 'Game Over - O wins'
    
