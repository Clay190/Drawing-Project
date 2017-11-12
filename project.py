#Clay Kynor
#11/1/17
#drawingProgram.py

from ggame import *

#constants
ROWS = 26
COLS = 50
CELL_SIZE = 20

#getting the coordinates of data numY to move one cell size to the right
#then checks whether the cursor should draw, or just sprite a box to the right of the current one, using the new X coordinates, and then remove the box to that new one's left (the old box)
def moveRight(event):
    if data['numX'] < (COLS)*CELL_SIZE:
        data['numX'] += CELL_SIZE
        boxAsset = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data['color']),data['color'])
        if data['onOff']%2==0:
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))
        else:
            data['lastBox'].destroy()
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))
            
#getting the coordinates of data numX to move on Cell size to the left
#checks whether the cursor is in drawing mode and then decides whether or not to destroy the last box before spriting the new both in a location cell to the left of the other box by using the new X coordinates
def moveLeft(event):
    if data['numX'] > 0:
        data['numX'] -= CELL_SIZE
        boxAsset = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data['color']),data['color'])
        if data['onOff']%2==0:
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))
        else:
            data['lastBox'].destroy()
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))

#getting coordinates of data numY to move one cell size up
#checks whether or not to destroy the last box it makes by checking if drawing is on or off, before placing a new box one cell above the old box by using the new Y coordinates
def moveUp(event):
    if data['numY'] > 0:
        data['numY'] -= CELL_SIZE
        boxAsset = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data['color']),data['color'])
        if data['onOff']%2==0:
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))
        else:
            data['lastBox'].destroy()
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))

#getting the coordinates of data numY to move one cell size down
#checks whether drawing is on or off and if drawing is off, then it removes the last box placed and then no matter what drawing is, it sprites a new box with the new Y coordinates
def moveDown(event):
    if data['numY'] < (ROWS)*CELL_SIZE: 
        data['numY'] += CELL_SIZE
        boxAsset = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data['color']),data['color'])
        if data['onOff']%2==0:
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))
        else:
            data['lastBox'].destroy()
            data['lastBox'] = Sprite(boxAsset, (data['numX'],data['numY']))
        
#a way of telling whether the user means to draw on the screen, or just move the cursor around
#it does this by tallying the number of times the user hits the 'd' key and then adding 1 to the variable data['onOff'] then it tells whether or not the user wants to draw or not by seeing if data['onOff'] is even or odd, and prints whether drawing is 'on' or drawing is 'off'
#after it is determind whether drawing is on (an even number) or off (an odd number), the moving of the cursor then takes the information of what the variable data['onOff'] is and uses that to determind whether to move the previous box placed
def drawingOnOff(event):
    data['onOff'] += 1
    if data['onOff']%2==0:
        print("on")
    else:
        print("off")
        
#Changes cursor (data['color']) to black
def changeColorBlack(event):
    data['color'] = black        

#Changes cursor (data['color']) to red
def changeColorRed(event):
    data['color'] = red
    
#Changes cursor (data['color']) to blue
def changeColorBlue(event):
    data['color'] = blue
    
#Changes cursor (data['color']) to green
def changeColorGreen(event):
    data['color'] = green

#Changes cursor (data['color']) to yellow    
def changeColorYellow(event):
    data['color'] = yellow
    
#Changes cursor (data['color']) to white (in case the user would like to erase thier previous work)
def changeColorErase(event):
    data['color'] = white

#runs the game section of the program
if __name__ == '__main__':
    
    data = {}
    data['numX'] = 0
    data['numY'] = 0
    data['onOff'] = 0
    
#color codes that we use for changing the color (lines 70-92)
    red = Color(0xFF0000,1)
    green = Color(0x00FF00,1)
    blue = Color(0x0000FF,1)
    black = Color(0x000000,1)
    yellow = Color(0xFFFF00,1)
    white = Color(0xFFFFFF, 1)
    
#sets a starting color for the cursor
    data['color'] = black
    
#tells what the cursor is going to look like, and what variables it is going to use apperance wise (color, size, shape)
    boxAsset = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data['color']),data['color'])

#setting a starting box to appear on screen before commands are pressed
    box = Sprite(boxAsset, (data['numX'],data['numY']))
    
#Running the actual program and listing for the press of a key in order to change something according to earlier code
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown) 
    App().listenKeyEvent('keydown', 'd', drawingOnOff)
    App().listenKeyEvent('keydown', 'q', changeColorBlack)
    App().listenKeyEvent('keydown', 'w', changeColorBlue)
    App().listenKeyEvent('keydown', 'e', changeColorGreen)
    App().listenKeyEvent('keydown', 'r', changeColorRed)
    App().listenKeyEvent('keydown', 't', changeColorYellow)
    App().listenKeyEvent('keydown', 'y', changeColorErase)
    
    App().run()
