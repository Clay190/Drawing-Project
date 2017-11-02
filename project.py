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
    if box.x < (COLS)*CELL_SIZE:
        box.x += CELL_SIZE

def moveLeft(event):
    if box.x > 0:
        box.x -= CELL_SIZE

def moveUp(event):
    if box.y > 0:
        box.y -= CELL_SIZE

def moveDown(event):
    if box.y < (ROWS)*CELL_SIZE: 
        box.y += CELL_SIZE
        ['numbox'] 
        
        
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

    box = Sprite(boxAsset)
    
    #Running the program
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown) 
    App().listenKeyEvent('keydown', 'd', drawingOnOff)
    App().run()
