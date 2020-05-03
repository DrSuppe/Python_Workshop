import pygame
import time
from main import gameOfLife
nRows = 40
nCollumns = 40


width = nRows * 10
height = nCollumns * 10

def draw(arr):
    for i in range(1, nRows-1):
        for j in range(1, nCollumns-1):
            if arr[i][j].nextState == False:
                pygame.draw.rect(screen, (255, 255, 255), (i*10, j*10, 10, 10))
                arr[i][j].state = arr[i][j].nextState
            else:
                pygame.draw.rect(screen, (0,0,0), (i*10, j*10, 10, 10))
                arr[i][j].state = arr[i][j].nextState


#-------------------------------------#-------------------------------------

test = gameOfLife(nRows, nCollumns)
test.createField()
#-------------------------------------#-------------------------------------



screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game Of Life - Python Workshop')
screen.fill((255,255,255)) # Hintergrund anmalen
pygame.display.flip() #"läd" den Bildschirm -> aktualisiert

while True:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          break
  pygame.display.flip()
  draw(test.arr)
  test.nextCycle()
  time.sleep(0.2)
  print("neueRunde")


