#Clay Kynor
#11/1/17
#drawingProgram.py

from ggame import *

#constants
ROWS = 26
COLS = 50
CELL_SIZE = 20

#getting the cursor to move to the right
#then checks whether the cursor should draw, or just sprite a box to the right and then 
def moveRight(event):
    if data['numX'] < (COLS)*CELL_SIZE:
        data['numX'] += CELL_SIZE
        boxAsset = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data['color']),data['color'])
        if data['onOff']%2==0:
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))
        else:
            data['lastBox'].destroy()
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))
            
#getting the cursor to move to the left
def moveLeft(event):
    if data['numX'] > 0:
        data['numX'] -= CELL_SIZE
        boxAsset = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data['color']),data['color'])
        if data['onOff']%2==0:
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))
        else:
            data['lastBox'].destroy()
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))

#getting the cursor to move to up
def moveUp(event):
    if data['numY'] > 0:
        data['numY'] -= CELL_SIZE
        boxAsset = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data['color']),data['color'])
        if data['onOff']%2==0:
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))
        else:
            data['lastBox'].destroy()
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))

#getting the cursor to move to the down
def moveDown(event):
    if data['numY'] < (ROWS)*CELL_SIZE: 
        data['numY'] += CELL_SIZE
        boxAsset = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data['color']),data['color'])
        if data['onOff']%2==0:
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))
        else:
            data['lastBox'].destroy()
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))
        
def drawingOnOff(event):
    data['onOff'] += 1
    if data['onOff']%2==0:
        print("on")
    else:
        print("off")
        
def changeColorBlack(event):
    data['color'] = black        

def changeColorRed(event):
    data['color'] = red
    
def changeColorBlue(event):
    data['color'] = blue
    
def changeColorGreen(event):
    data['color'] = green

#runs the game
if __name__ == '__main__':
    
    data = {}
    data['numX'] = 0
    data['numY'] = 0
    data['onOff'] = 0
    
    #colors
    red = Color(0xFF0000,1)
    green = Color(0x00FF00,1)
    blue = Color(0x0000FF,1)
    black = Color(0x000000,1)
    white = Color(0xFFFFFF, 1)
    
    data['color'] = black
    
    boxAsset = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data['color']),data['color'])

    box = Sprite(boxAsset, (data['numX'],data['numY']))
    
    data['lastBox'] = box
    
    #Running the program
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown) 
    App().listenKeyEvent('keydown', 'd', drawingOnOff)
    App().listenKeyEvent('keydown', 'q', changeColorBlack)
    App().listenKeyEvent('keydown', 'w', changeColorBlue)
    App().listenKeyEvent('keydown', 'e', changeColorGreen)
    App().listenKeyEvent('keydown', 'r', changeColorRed)
    
    App().run()
