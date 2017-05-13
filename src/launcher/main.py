import sys, pygame
from pygame.transform import scale
pygame.init()

size = width, height = 1024, 768
gray = 100, 100, 100

screen = pygame.display.set_mode(size)

pygame.display.set_caption('Athenas')

buttons = pygame.image.load("buttons.png")
buttons = pygame.transform.scale(buttons, (512, 512))

opcionesRect = (0, 0, 128, 64)

opcionesPos = (32, 512)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    screen.fill(gray)
    screen.blit(buttons, opcionesPos, opcionesRect)
    pygame.display.flip()