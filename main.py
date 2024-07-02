from enum import Enum
import pygame as pg
import asyncio
from random import randint as rand

from settings import *

from Scripts.spaceship import SpaceShip
from Scripts.planet import Planet

from Scripts.utils import planets_overlap



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
        self.world = pg.Surface(WORLDSIZE)


        #sprites
        self.all_sprites = pg.sprite.Group()
        self.spaceship = SpaceShip()

        self.clock = pg.time.Clock()

        self.spawn_planets()

        self.all_sprites.add(self.spaceship)

    def spawn_planets(self):
        self.planets = pg.sprite.Group()
        num_planets = rand(50,100)
        max_attempts = 100
        spaceship_width = self.spaceship.rect.width
        for _ in range(num_planets):
            for attempt in range(max_attempts):
                
                radius = rand(spaceship_width,spaceship_width*3)
                center = (rand(radius,WORLDSIZE[0]-radius),
                          rand(radius,WORLDSIZE[1]-radius))
                new_planet = Planet(radius,center)

                overlap = False
                for planet in self.planets:
                    if planets_overlap(planet,new_planet,self.spaceship):
                        overlap = True
                        break
                
                if self.spaceship.collide_planet(new_planet):
                    overlap = True
                
                
                
                if not overlap:
                    self.planets.add(new_planet)
                    self.all_sprites.add(new_planet)
                    break
                else:
                    new_planet.kill()
                
        
    def check_planet_collisions(self):
        for planet in self.planets:
            if self.spaceship.collide_planet(planet):
                self.hovered_planet = planet
                

       

    def draw_space(self,dt):
        self.main_window.fill(-1)
        self.world.fill(1)
        
         


        #update sprites
        self.all_sprites.update(dt)
        self.all_sprites.draw(self.world)
        self.main_window.blit(self.world,self.spaceship.viewcords)

        pg.display.flip()
    
    async def loop(self):
        self.running = True
        while self.running:
            dt = self.clock.tick(FPS) / 1000
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            
            if self.game_state == GameState.SPACE:
                self.draw_space(dt)
                self.hovered_planet = None
                self.check_planet_collisions()
            
            


            self.clock.tick(FPS)
            
            await asyncio.sleep(0)




pg.init()

window = pg.display.set_mode((WIDTH,HEIGHT))
game = Game(window)
asyncio.run(game.loop())