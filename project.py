#Clay Kynor
#12/14/17
#FinalProject.py - OTHELLO

from ggame import *

RADIUS = 30
LINESIZE = 1.4
P1COLOR = Color(0xFFFFFF,1)
P2COLOR = Color(0x000000,1)
BOARDCOLOR = Color(0x999999,0.5)
BLACK = Color(0x000000,1)

P1CIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),P1COLOR)
P2CIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),P2COLOR)
BOARDCIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),BOARDCOLOR)

def buildBoard():
    for i in range(0,8):
        data['board'].append(['']*8)
    #Main center point
    data['board'][3][3] = 1
    #Tests East/West
    data['board'][4][3] = 2
    data['board'][5][3] = 2
    data['board'][6][3] = 2
    data['board'][2][3] = 2
    data['board'][7][3] = 1
    data['board'][0][3] = 1
    data['board'][3][0] = 1
    #Tests North/South
    data['board'][3][7] = 1
    data['board'][3][6] = 2
    data['board'][3][5] = 2
    data['board'][3][4] = 2
    data['board'][3][2] = 2
    data['board'][3][1] = 2
    data['board'][1][3] = 2
    #Tests SouthEast/NorthWest
    data['board'][0][0] = 1
    data['board'][1][1] = 2
    data['board'][2][2] = 2
    data['board'][4][4] = 2
    data['board'][5][5] = 2
    data['board'][6][6] = 2
    data['board'][7][7] = 1
    #Tests SouthWest/NorthEast
    data['board'][0][6] = 1
    data['board'][6][0] = 1
    data['board'][2][4] = 2
    data['board'][1][5] = 2
    data['board'][4][2] = 2
    data['board'][5][1] = 2
    return data['board']

def boardFull():
    for i in range(0,8):
        if '' in data['board'][i]:
            print('board is not full')
            return False
    else:
        print('board is full')
        return True
 
def winner():
    p1Points = 0
    p2Points = 0
    for row in range(0,8):
        for col in range(0,8):
            if data['board'][row][col] == 1:
                p1Points += 1
            elif data['board'][row][col] == 2:
                p2Points += 1
    print("Player 1 has", p1Points)
    print("Player 2 has", p2Points)
    if p1Points>p2Points:
        print('Player 1 wins!')
    elif p1Points<p2Points:    
        print('Player 2 wins!')
    else:
        print("This game is a draw!")
    
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,8):
        for col in range(0,8):
            if data['board'][row][col] == '':
                Sprite(BOARDCIRCLE,(RADIUS+(row*(RADIUS*2)),RADIUS+(col*RADIUS*2)))
            elif data['board'][row][col] == 1:
                Sprite(P1CIRCLE,((row*RADIUS*2)+RADIUS,RADIUS+(col*RADIUS*2)))
            else:
                Sprite(P2CIRCLE,((row*RADIUS*2)+RADIUS,RADIUS+(col*RADIUS*2)))
                
def flipNorth(x,y):
    i=1
    m=0
    while data['board'][x][y-i] == 2:
        i+=1
        m+=1
    if data['board'][x][y-i] != '':
        data['board'][x][y-i] = 1
        for t in range(m+1):
            data['board'][x][y-t] = 1
    redrawAll()

def flipSouth(x,y):
    i=1
    m=0
    while data['board'][x][y+i] == 2:
        i+=1
        m+=1
    if data['board'][x][y+i] != '':
        data['board'][x][y+i] = 1
        for t in range(m+1):
            data['board'][x][y+t] = 1
    redrawAll()

def flipEast(x,y):
    i=1
    m=0
    while data['board'][x+i][y] == 2:
        i+=1
        m+=1
    if data['board'][x+i][y] != '':
        data['board'][x+i][y] = 1
        for t in range(m+1):
            data['board'][x+t][y] = 1
    redrawAll()

def flipWest(x,y):
    i=1
    m=0
    while data['board'][x-i][y] == 2:
        i+=1
        m+=1
    if data['board'][x-i][y] != '':
        data['board'][x-i][y] = 1
        for t in range(m+1):
            data['board'][x-t][y] = 1
'''
def flipNorthEast(x,y):
    i=1
    while data['board'][x+i][y-i] == 2:
        print(i)
        i+=1
    if data['board'][x+i][y-i] != '':
        data['board'][x+i][y-i] = 1
        redrawAll()

def flipNorthWest(x,y):
    i=1
    while data['board'][x-i][y-i] == 2:
        print(i)
        i+=1
    if data['board'][x-i][y-i] != '':
        data['board'][x-i][y-i] = 1
        redrawAll()
    
def flipSouthEast(x,y):
    i=1
    while data['board'][x+i][y+i] == 2:
        print(i)
        i+=1
    if data['board'][x+i][y+i] != '':
        data['board'][x+i][y+i] = 1
        redrawAll()

def flipSouthWest(x,y):
    i=1
    while data['board'][x-i][y+i] == 2:
        print(i)
        i+=1
    if data['board'][x-i][y+i] != '':
        data['board'][x-i][y+i] = 1
    redrawAll()
'''
def flipPieces(x,y):
    print('Do flipPieces function')
    
if __name__ == '__main__':
    
    data = {}
    data['board'] = []
    data['row'] = 3
    data['col'] = 3
    
    buildBoard()
    print(data['board'])
    flipPieces(data['row'],data['col'])
    #flipEast(data['row'],data['col'])
    print(data['board'])
    redrawAll()
    boardFull()
    winner()
    App().run()