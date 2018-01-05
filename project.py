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
    data['board'][4][3] = 2
    data['board'][3][4] = 2
    data['board'][4][4] = 1
    return data['board']

def boardFull():
    for i in range(0,8):
        if '' in data['board'][i]:
            return False
    else:
        print('board is full')
        winner()
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
                Sprite(BOARDCIRCLE,(RADIUS+(col*(RADIUS*2)),RADIUS+(row*RADIUS*2)))
            elif data['board'][row][col] == 1:
                Sprite(P1CIRCLE,((col*RADIUS*2)+RADIUS,RADIUS+(row*RADIUS*2)))
            else:
                Sprite(P2CIRCLE,((col*RADIUS*2)+RADIUS,RADIUS+(row*RADIUS*2)))
                
def flipNorth(x,y):
    i=1
    m=0
    if data['turn']%2 == 0:
        if 8>x>-1 and 8>y>-1:
            while data['board'][x][y-i] == 2:
                i+=1
                m+=1
            if data['board'][x][y-i] != '':
                data['board'][x][y-i] = 1
                for t in range(m+1):
                    data['board'][x][y-t] = 1
    else:
        if 8>x>-1 and 8>y>-1:
            while data['board'][x][y-i] == 1:
                i+=1
                m+=1
            if data['board'][x][y-i] != '':
                data['board'][x][y-i] = 2
                for t in range(m+1):
                    data['board'][x][y-t] = 2
    redrawAll()

def flipSouth(x,y):
    i=1
    m=0
    if data['turn']%2 == 0:
        if 8>x>-1 and 8>y>-1:    
            while data['board'][x][y+i] == 2:
                i+=1
                m+=1
            if data['board'][x][y+i] != '':
                data['board'][x][y+i] = 1
                for t in range(m+1):
                    data['board'][x][y+t] = 1
    else:
        if 8>x>-1 and 8>y>-1:
            while data['board'][x][y+i] == 1:
                i+=1
                m+=1
            if data['board'][x][y+i] != '':
                data['board'][x][y+i] = 2
                for t in range(m+1):
                    data['board'][x][y+t] = 2

def flipEast(x,y):
    i=1
    m=0
    if data['turn']%2 == 0:    
        if 8>x>-1 and 8>y>-1:
            while data['board'][x+i][y] == 2:
                i+=1
                m+=1
            if data['board'][x+i][y] != '':
                data['board'][x+i][y] = 1
                for t in range(m+1):
                    data['board'][x+t][y] = 1
    else:
        if 8>x>-1 and 8>y>-1:
            while data['board'][x+i][y] == 1:
                i+=1
                m+=1
            if data['board'][x+i][y] != '':
                data['board'][x+i][y] = 2
                for t in range(m+1):
                    data['board'][x+t][y] = 2

def flipWest(x,y):
    i=1
    m=0
    if data['turn']%2 == 0:    
        if 8>x>-1 and 8>y>-1:
            while data['board'][x-i][y] == 2:
                i+=1
                m+=1
            if data['board'][x-i][y] != '':
                data['board'][x-i][y] = 1
                for t in range(m+1):
                    data['board'][x-t][y] = 1
    else:
        if 8>x>-1 and 8>y>-1:
            while data['board'][x-i][y] == 1:
                i+=1
                m+=1
            if data['board'][x-i][y] != '':
                data['board'][x-i][y] = 2
                for t in range(m+1):
                    data['board'][x-t][y] = 2

def flipNorthEast(x,y):
    i=1
    m=0
    if data['turn']%2 == 0:    
        if 8>x>-1 and 8>y>-1:
            while data['board'][x+i][y-i] == 2:
                i+=1
                m+=1
            if data['board'][x+i][y-i] != '':
                data['board'][x+i][y-i] = 1
                for t in range(m+1):
                    data['board'][x+t][y-t] = 1
    else:
        if 8>x>-1 and 8>y>-1:
            while data['board'][x+i][y-i] == 1:
                i+=1
                m+=1
            if data['board'][x+i][y-i] != '':
                data['board'][x+i][y-i] = 2
                for t in range(m+1):
                    data['board'][x+t][y-t] = 2


def flipNorthWest(x,y):
    i=1
    m=0
    if data['turn']%2 == 0:
        if 8>x>-1 and 8>y>-1:
            while data['board'][x-i][y-i] == 2:
                i+=1
                m+=1
            if data['board'][x-i][y-i] != '':
                data['board'][x-i][y-i] = 1
                for t in range(m+1):
                    data['board'][x-t][y-t] = 1
    else:
        if 8>x>-1 and 8>y>-1:
            while data['board'][x-i][y-i] == 1:
                i+=1
                m+=1
            if data['board'][x-i][y-i] != '':
                data['board'][x-i][y-i] = 2
                for t in range(m+1):
                    data['board'][x-t][y-t] = 2 
            
        
def flipSouthEast(x,y):
    i=1
    m=0
    if data['turn']%2==0:
        if 8>x>-1 and 8>y>-1:
            while data['board'][x+i][y+i] == 2:
                i+=1
                m+=1
            if data['board'][x+i][y+i] != '':
                data['board'][x+i][y+i] = 1
                for t in range(m+1):
                    data['board'][x+t][y+t] = 1
    else:
        if 8>x>-1 and 8>y>-1:
            while data['board'][x+i][y+i] == 1:
                i+=1
                m+=1
            if data['board'][x+i][y+i] != '':
                data['board'][x+i][y+i] = 2
                for t in range(m+1):
                    data['board'][x+t][y+t] = 2
                
def flipSouthWest(x,y):
    i=1
    m=0
    if data['turn']%2 == 0:
            if 8>x>-1 and 8>y>-1:
                while data['board'][x+i][y-i] == 2:
                    i+=1
                    m+=1
                if data['board'][x-i][y+i] != '':
                    data['board'][x-i][y+i] = 1
                    for t in range(m+1):
                        data['board'][x-t][y+t] = 1
    else:
        if 8>x>-1 and 8>y>-1:    
            while data['board'][x-i][y+i] == 1:
                i+=1
                m+=1
            if data['board'][x-i][y+i] != '':
                data['board'][x-i][y+i] = 2
                for t in range(m+1):
                    data['board'][x-t][y+t] = 2
        
def mouseClick(event):
    row = int(event.y/(2*RADIUS))
    col = int(event.x/(2*RADIUS))
    if data['turn']%2 == 0:
        data['board'][row][col] = 2
    else:
        data['board'][row][col] = 1
    data['turn']+=1
    flipPieces(row,col)
    

def flipPieces(x,y):
    flipNorth(x,y)
    flipSouth(x,y)
    flipEast(x,y)
    flipWest(x,y)
    flipNorthEast(x,y)
    flipSouthEast(x,y)
    flipNorthWest(x,y)
    flipSouthWest(x,y)
    redrawAll()
    boardFull()
    
if __name__ == '__main__':
    
    data = {}
    data['board'] = []
    data['row'] = 0
    data['col'] = 0
    data['turn'] = 0
    
    buildBoard()
    flipNorthEast(data['row'],data['col'])
    redrawAll()
    App().listenMouseEvent("click", mouseClick)
    App().run()