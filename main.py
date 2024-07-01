from enum import Enum
import pygame as pg
import asyncio

from settings import *



class GameState(Enum):
    MENU = 0
    EXPLORE = 1



class Game:
    def __init__(self,main_window):
        self.main_window = main_window
        self.game_state = GameState.EXPLORE.value
        
        self.running = False
    

    def draw(self):
        self.main_window.fill(1)

        #update sprites
        #draw sprites

        pg.display.flip()
    
    async def loop(self):
        self.running = True
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            
            self.draw()
            await asyncio.sleep(0)




pg.init()

window = pg.display.set_mode((WIDTH,HEIGHT))
game = Game(window)
asyncio.run(game.loop())