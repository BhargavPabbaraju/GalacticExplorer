import pygame as pg
from pygame.math import Vector2 as vec2

from random import randint as rand


class Planet(pg.sprite.Sprite):
    def __init__(self,radius,center):
        super().__init__()
        
        self.position = vec2(center)

        self.angle = 0

        self.image = pg.Surface((radius*2,radius*2),pg.SRCALPHA)
        pg.draw.circle(self.image,
                      (rand(0,255),rand(0,255),rand(0,255)),
                      (radius,radius),radius)

        self.rect = self.image.get_rect(center=center)

        self.radius = radius
        
        
        
