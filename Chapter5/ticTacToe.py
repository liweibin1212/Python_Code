theBoard ={'topL':' ','topM':' ','topR':' ','midL':' ','midM':' ','midR':' ',
           'lowL':' ','lowM':' ','lowR':' '}
#for i in theBoard.items():
#    print(i)
def printBoard(Board):
    print(Board['topL']+'|'+Board['topM']+'|'+Board['topR'])
    print('-+-+-')
    print(Board['midL']+'|'+Board['midM']+'|'+Board['midR'])
    print('-+-+-')
    print(Board['lowL']+'|'+Board['lowM']+'|'+Board['lowR'])
#printBoard(theBoard)

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + ' Move to which space: topL,topM,topR,lowL,lowM,lowR,midL,midM,midR')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)