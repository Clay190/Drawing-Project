#Clay Kynor
#11/1/17
#drawingProgram.py

from ggame import *

#constants
ROWS = 26
COLS = 50
CELL_SIZE = 20

#getting the cursor to move
def moveRight(event):
    if box.x < (COLS-1)*CELL_SIZE:
        box.x += CELL_SIZE

def moveLeft(event):
    if box.x > 0:
        box.x -= CELL_SIZE

def moveUp(event):
    if box.y > 0:
        box.y -= CELL_SIZE

def moveDown(event):
    if box.y < (ROWS-1)*CELL_SIZE: 
        box.y += CELL_SIZE
        
#runs the game
if __name__ == '__main__':
    
    #colors
    red = Color(0xFF0000,1)
    green = Color(0x00FF00,1)
    blue = Color(0x0000FF,1)
    black = Color(0x000000,1)
    
    boxAsset = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),black)

    box = Sprite(boxAsset)
    
    #Running the program
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown)    
    App().run()
