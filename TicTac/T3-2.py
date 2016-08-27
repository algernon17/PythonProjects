#!/usr/bin/env python
# Tic-Tac-Toe 1
#    note a comma at the end of the print suppresses the newline

board = [ 'O', 'X', ' ' , 'O', ' ', 'X', 'O', 'X', 'X' ]
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
    
if __name__ == '__main__':
    printBoard()
