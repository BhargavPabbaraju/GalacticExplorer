from enum import Enum
import pygame as pg
import asyncio
from random import randint as rand

from settings import *

from Scripts.spaceship import SpaceShip



class GameState(Enum):
    MENU = 0
    SPACE = 1



class Game:
    def __init__(self,main_window):
        #attributes
        self.game_state = GameState.SPACE
        self.running = False

        #surfaces
        self.main_window = main_window
        self.world = pg.Surface(WORLDSIZE,pg.SRCALPHA)


        #sprites
        self.all_sprites = pg.sprite.Group()
        self.spaceship = SpaceShip(self.all_sprites)

        self.clock = pg.time.Clock()

       

    def draw_space(self):
        self.main_window.fill(-1)
        self.world.fill(-1)
        
         #temp
        self.world.blit(pg.Surface((100,100)),(2000,6000))


        #update sprites
        self.all_sprites.update()
        self.all_sprites.draw(self.world)
        self.main_window.blit(self.world,self.spaceship.viewcords)

        pg.display.flip()
    
    async def loop(self):
        self.running = True
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            
            if self.game_state == GameState.SPACE:
                self.draw_space()
            

            self.clock.tick(FPS)
            
            await asyncio.sleep(0)




pg.init()

window = pg.display.set_mode((WIDTH,HEIGHT))
game = Game(window)
asyncio.run(game.loop())