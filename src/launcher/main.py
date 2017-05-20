# TODO:
#   - Fix buttons position bug.

import pygame, tns
from pygame.locals import *

pygame.init()

# Variables for screen size and color
size = [1024, 768]
gray = 100, 100, 100

# Create screen object
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

# Load Icon
icon = pygame.image.load('icon/icon32.png')

# Set window title and icon
pygame.display.set_caption('Athenas')
pygame.display.set_icon(icon)

# Load menu sprite sheet
menuSpr = pygame.image.load("buttons.png")
menuSpr = pygame.transform.scale(menuSpr, (1024, 1024))

# Pre-render screen
pygame.display.flip()

# Declare nao's
jugarBtn    = tns.tnsNao([32 , size[1] - 186 ], [0 , 15*4 , 45*4 , 15*4 ], menuSpr, True)
opcionesBtn = tns.tnsNao([32 , size[1] - 124 ], [0 , 0    , 45*4 , 15*4 ], menuSpr, True)
salirBtn    = tns.tnsNao([32 , size[1] - 62  ], [0 , 30*4 , 31*4 , 15*4 ], menuSpr, True)

opcionesMen   = tns.tnsNao([32, 32], [45*4, 0, 175*4, 131*4], menuSpr, False)
opcionesClose = tns.tnsNao(\
[(opcionesMen.tnsPos[0] + opcionesMen.tnsSize[0]) - 13*4, opcionesMen.tnsPos[1]],\
    [32*4, 30*4, 13*4, 13*4],\
menuSpr, False)
opcionesWin   = [opcionesMen, opcionesClose] 

def getSize():
    return size

# Render function
def render():

    screen.fill(gray)

    salirBtn.tnsDraw(screen)
    jugarBtn.tnsDraw(screen)
    opcionesBtn.tnsDraw(screen)
    opcionesMen.tnsDraw(screen)
    opcionesClose.tnsDraw(screen)

    pygame.display.flip()

def getSize():
    return size

# Infinite loop
while 1:

    for event in pygame.event.get():

#       Exit when X is clicked
        if event.type == pygame.QUIT: tns.exitGame()

#       Re-render the screen when it's resized
        if event.type == VIDEORESIZE:
            size = [event.w, event.h]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

#       Detect if mouse is released
        if event.type == MOUSEBUTTONUP:
            if salirBtn.tnsClick(event.pos):
                tns.exitGame()
            if opcionesBtn.tnsClick(event.pos):
                for i in opcionesWin:
                    i.toRender = True
            if opcionesClose.tnsClick(event.pos):
                for i in opcionesWin:
                    i.toRender = False
    
    jugarBtn
#   Call render function
    render()