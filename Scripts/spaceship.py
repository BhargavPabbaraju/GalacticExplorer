import pygame as pg
from settings import *
from pygame.math import Vector2 as vec2

SPACESHIP_SIZE = (WIDTH//4,HEIGHT//4)

#Position the spaceship on the bottom center of world
SPACESHIP_POS = (
    WORLDSIZE[0]//2,
    WORLDSIZE[1]- SPACESHIP_SIZE[1]//2,
    )

SPACESHIP_SPEED = 5 #degrees per frame

class SpaceShip(pg.sprite.Sprite):
    def __init__(self,groups,size=SPACESHIP_SIZE,position=SPACESHIP_POS):
        super().__init__(groups)
        self.size = size
        self.position = vec2(position)

        self.image = pg.Surface(self.size)
        self.image.fill(Color.GREEN.value)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        
        self.active = True
        
        self.speed = SPACESHIP_SPEED

        self.origPosition = vec2(position)
    

    def update(self):

        if self.active:
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.position.x -= self.speed
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.position.x += self.speed
            if keys[pg.K_UP] or keys[pg.K_w]:
                self.position.y -= self.speed
               
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                
                if self.position.y >= self.origPosition.y:
                    self.position.y = self.origPosition.y
                else:
                    self.position.y += self.speed
            

        


        self.rect.center = self.position

        
        #Update the world position based on spaceship position
        self.viewcords = (
            #spaceship must be at the center of the camera
            - (self.rect.centerx - WIDTH//2)
            ,
            #spaceship must be stuck at the bottom of the camera
            - (self.rect.bottom - HEIGHT)
        )