'''
Created on Jan 24, 2019

@author: Nik
'''
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
moves =['X','Y']

print('Coordaintes for the board')
for k in theBoard.keys():
    print (k)
print('top, mid, or low refers to the rows on the board')
print('L, M, or R refers to the columns on the board (Left, Mid, or Right)')


def quitscreen():
    
    print('enter y to play again or enter n to quit')
    quit_user=input()
    if quit_user == 'y':
        first()
        
    if quit_user == 'n':
        exit()
    else:
        quitscreen()

def tiescreen():
    print('Tie')
    quitscreen()

def printBoard(board):
    
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    
def endscreen():
    print("game over" )
    global turn 
    if turn == 'X':            
        turn = 'O'
    else:
        turn = 'X' 
    print("the winner is " + turn )
    
    quitscreen()
        
def wincondition(theBoard):
    if theBoard['top-L'] == 'X' and theBoard['top-M'] == 'X' and theBoard['top-R'] == 'X' or theBoard['top-L'] == 'O' and theBoard['top-M'] == 'O' and theBoard['top-R'] == 'O' :
        
        endscreen()

    if theBoard['mid-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['mid-R'] == 'X' or theBoard['mid-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['mid-R'] == 'O' :
        endscreen()

    if theBoard['low-L'] == 'X' and theBoard['low-M'] == 'X' and theBoard['low-R'] == 'X' or theBoard['low-L'] == 'O' and theBoard['low-M'] == 'O' and theBoard['low-R'] == 'O' :
          
        endscreen()
  
    if theBoard['top-L'] == 'X' and theBoard['mid-L'] == 'X' and theBoard['low-L'] == 'X' or theBoard['top-L'] == 'O' and theBoard['mid-L'] == 'O' and theBoard['low-L'] == 'O':
          
        endscreen()
        
    if theBoard['top-M'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-M'] == 'X' or theBoard['top-M'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-M'] == 'O':
          
        endscreen()
        
    if theBoard['top-R'] == 'X' and theBoard['mid-R'] == 'X' and theBoard['low-R'] == 'X' or theBoard['top-R'] == 'O' and theBoard['mid-R'] == 'O' and theBoard['low-R'] == 'O':
          
        endscreen()
    if theBoard['top-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-R'] == 'X' or theBoard['top-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-R'] == 'O':
        endscreen()
    if theBoard['top-R'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-L'] == 'X' or theBoard['top-R'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-L'] == 'O':
        endscreen()

        
def first():

    moves =['X','Y']
    print('does X or O go first?')
    global turn
    turn=str(input())
    if turn not in moves:
        print ('that was an invalid command')
        first()
    if turn in moves:
        
        
        theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    
        printBoard(theBoard)
        for i in range(10):
       
       
            if i==9:
                tiescreen()
       
            
            print('Turn for ' + turn + '. Move on which space?')
        
            move = input()    
            if move not in theBoard:
                print('that was an invalid command')
                i - 1 
                printBoard(theBoard)
          
            if move in theBoard:
            
            
                theBoard[move] = turn   

                if turn == 'X':            
                    turn = 'O'
                else:
                    turn = 'X'
                printBoard(theBoard)
                wincondition(theBoard)

first()
        



   
    
    



