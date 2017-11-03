#Clay Kynor
#11/1/17
#drawingProgram.py

from ggame import *

#constants
ROWS = 25
COLS = 50
CELL_SIZE = 20

#getting the cursor to move
def moveRight(event):
    if data['numX'] < (COLS)*CELL_SIZE:
        data['numX'] += CELL_SIZE
        Sprite(boxAsset, (data['numX'],data['numY']))

def moveLeft(event):
    if data['numX'] > 0:
        data['numX'] -= CELL_SIZE
        Sprite(boxAsset, (data['numX'],data['numY']))

def moveUp(event):
    if data['numY'] > 0:
        data['numY'] -= CELL_SIZE
        Sprite(boxAsset, (data['numX'],data['numY']))

def moveDown(event):
    if data['numY'] < (ROWS)*CELL_SIZE: 
        data['numY'] += CELL_SIZE
        Sprite(boxAsset, (data['numX'],data['numY']))
        
def drawingOnOff(event):
    print('d')
        
#runs the game
if __name__ == '__main__':
    
    data = {}
    data['numX'] = 0
    data['numY'] = 0
    
    #colors
    red = Color(0xFF0000,1)
    green = Color(0x00FF00,1)
    blue = Color(0x0000FF,1)
    black = Color(0x000000,1)
    
    color = black
    
    boxAsset = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,color),color)

    box = Sprite(boxAsset, (data['numX'],data['numY']))
    
    #Running the program
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown) 
    App().listenKeyEvent('keydown', 'd', drawingOnOff)
    App().run()
