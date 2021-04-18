import pygame
import time
from Spiellogik import GameOfLife
from pygame.locals import *

nRows = 70
nCollumns = 70


width = nRows * 10
height = nCollumns * 10

def draw(Spielfeld):
    for i in range(1, nRows-1):
        for j in range(1, nCollumns-1):
            if Spielfeld[i][j].naechsterStatus == True:
                pygame.draw.rect(screen, (255, 255, 255), (i*10, j*10, 10, 10))
                Spielfeld[i][j].status = Spielfeld[i][j].naechsterStatus
            else:
                pygame.draw.rect(screen, (0,0,0), (i*10, j*10, 10, 10))
                Spielfeld[i][j].status = Spielfeld[i][j].naechsterStatus


#-------------------------------------#-------------------------------------

test = GameOfLife(nRows, nCollumns)
test.erstelleSpielfeld()
#-------------------------------------#-------------------------------------



screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game Of Life - Python Workshop')
screen.fill((0,0,0)) # Hintergrund anmalen
pygame.display.flip() #"lädt" den Bildschirm -> aktualisiert

runningBed = True

while runningBed:
    for event in pygame.event.get():
        #print('event found')
        if event.type == pygame.QUIT: #KEYDOWN and event.key == pygame.K_q:
            #print('q pressed')
            runningBed = False

    test.naechsterSchritt()
    draw(test.spielfeld)
    pygame.display.flip()

    time.sleep(0.2)

