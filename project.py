#Clay Kynor
#12/14/17
#FinalProject.py - OTHELLO

from ggame import *

#Constants in the program, these values can be changed and adjusted to change the visuals of the game
RADIUS = 40
LINESIZE = 1.4
P1COLOR = Color(0xFFFFFF,1)
P2COLOR = Color(0x000000,1)
BOARDCOLOR = Color(0x999999,0.5)
BLACK = Color(0x000000,1)

#Equations for the circles using the constants
P1CIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),P1COLOR)
P2CIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),P2COLOR)
BOARDCIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),BOARDCOLOR)

def buildBoard():
    for i in range(0,8):
        data['board'].append(['']*8)
    #Main center point/sets up the starting 2x2 matrix of the board
    data['board'][3][3] = 1
    data['board'][4][3] = 2
    data['board'][3][4] = 2
    data['board'][4][4] = 1
    return data['board']

#Function that checks whether or not the board is full. If it is, it plays the winner function and also returns false.
def boardFull():
    for i in range(0,8):
        if '' in data['board'][i]:
            return False
    else:
        print('board is full')
        winner()
        return True

#After the board is full, this function counts up the number of pieces each player has and checks as to which player had more and therefore wins.
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
    
#This function is used everytime flipPieces function plays and it checks as to what entries (1,2,'') and then sprites the corresponding circle in the matrix    
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

#Checks whether there are peices of the other color in between a previously placed peice and the peice most recently placed. This paticular function checks whether there are pieces of the other color above the last peice.                
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

#Checks whether there are peices of the other color in between a previously placed peice and the peice most recently placed. This paticular function checks whether there are pieces of the other color below the last peice.
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

#Checks whether there are peices of the other color in between a previously placed peice and the peice most recently placed. This paticular function checks whether there are pieces of the other color to the right of the last peice.
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

#Checks whether there are peices of the other color in between a previously placed peice and the peice most recently placed. This paticular function checks whether there are pieces of the other color to the left of the last peice.
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
                    
#Checks whether there are peices of the other color in between a previously placed peice and the peice most recently placed. This paticular function checks whether there are pieces of the other color to the right and above the last peice.
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

#Checks whether there are peices of the other color in between a previously placed peice and the peice most recently placed. This paticular function checks whether there are pieces of the other color to the left and above the last peice.
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
            
#Checks whether there are peices of the other color in between a previously placed peice and the peice most recently placed. This paticular function checks whether there are pieces of the other color to the right and below the last peice.
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

#Checks whether there are peices of the other color in between a previously placed peice and the peice most recently placed. This paticular function checks whether there are pieces of the other color to the left and below of the last peice.
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
                    
#When the mouse is clicked, this function checks the x coordinate and y coordinate of where the mouse was clicked and then places a peice in that square. It checks what turn it is by seeing if the data['turn'] is even or odd. Then it updates the data['turn'] variable and it runs the flipPeices function using the x and y coordinates of the mouse click.
def mouseClick(event):
    row = int(event.y/(2*RADIUS))
    col = int(event.x/(2*RADIUS))
    if data['turn']%2 == 0:
        data['board'][row][col] = 2
    else:
        data['board'][row][col] = 1
    data['turn']+=1
    flipPieces(row,col)
    
#Runs all the individual flip functions and then redraws the whole board and checks to see whether or not the board is full by using the redrawAll and boardFull functions.
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
    
#Where all of the non functions are, where the actual game portion of the program is.
if __name__ == '__main__':
    
    #These are all of our variables kept in this data library. These variables include the matrix for the board, the row and column of the 
    data = {}
    data['board'] = []
    data['turn'] = 0
    
    #Calls upon the buildBoard function to create the starting board, and then sprites that board with the redrawAll function
    buildBoard()
    redrawAll()
    #Listens for a mouseclick and then when a mouseclick occurs it starts the mouseClick function
    App().listenMouseEvent("click", mouseClick)
    #Runs the program
    App().run()