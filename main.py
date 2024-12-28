import pygame,sys,random
from pygame.math import  Vector2 

class FRUIT:
  def __init__(self):
    self.x = random.randint(0,cell_number-1)
    self.y = random.randint(0,cell_number-1)
    self.pos = Vector2(self.x,self.y)
    #create a x and y position
    #draw a sqaure
  def draw_fruit(self):
    #draw rectangle
    fruit_rect = pygame.Rect(self.x*cell_size,self.y*ce
    pygame.draw.rect(screen,(126,166,114),fruit_rect) #
    

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size
clock = pygame.time.Clock()


fruit =  FRUIT()


while True:
  for event in pygame.event.get():
  # to close the program
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  screen.fill((175,215,70))
  fruit.draw_fruit()
  pygame.display.update()
  #ading FPS
  clock.tick(60)
