# Imports
import sdl2.ext
import sdl2
import ctypes
from bird import bird
from pipe import pipe
from floor import floor
from entity import entity
from background import background
import time
import random

background_img = b"../assets/background.png"


class scene(entity):

    def __init__(self):
        entity.__init__(self)
        self.event = sdl2.SDL_Event()
        self.type = None
        self.entities = None    # List containing all of the scene's entities
        self.background = None
        self.floor = None
        self.pipe1 = None
        self.pipe2 = None
        self.player = None
        self.index_player = None
        pass

    def process_events(self):
        if self.type == "game":
            while sdl2.SDL_PollEvent(ctypes.byref(self.event)) != 0:
                if self.event.type == sdl2.SDL_QUIT:
                    self.stop_entities()
                    break
                if self.event.type == sdl2.SDL_KEYDOWN:
                    if self.event.key.keysym.sym == sdl2.SDLK_SPACE:
                        if not self.player.is_alive():
                            self.player.start()
                            pass
                        self.player.flap()
                        pass
                pass
        if self.type == "menu":
            pass
        pass

    def init_as_game(self, rend):
        if rend is not None:
            self.type = "game"
            self.background = background(rend)
            self.floor = floor(rend)
            self.pipe1 = pipe(rend)
            self.pipe2 = pipe(rend)
            self.player = bird(rend)
            self.pipe2.surface.x = 1000
            self.entities = [self.background, self.pipe1, self.pipe2, self.floor, self.player]
            self.index_player = self.entities.index(self.player)
            self.start()
        else:
            self.player.surface.x = 80
            self.player.surface.y = 270
            self.pipe1.surface.x = 650
            self.pipe2.surface.x = 1000
            self.background.surface.x = 0
            self.background.surface.y = 0
            self.floor.surface.x = 0
        pass

    def init_as_menu(self, rend):
        self.type = "menu"
        pass

    def run(self):
        self.Running = True
        while self.Running:
            if self.type == "game":
                self.scroll_level()
                self.detect_collisions()
                time.sleep(0.0175)
                pass
            pass
        pass

    def stop_entities(self):
        for i in self.entities:
            i.stop()
            if i.is_alive():
                i.join()
        pass
        self.Running = False

    def detect_collisions(self):
        x_collide = False
        y_collide = False
        if self.player.surface.x + self.player.surface.w - 15 >= self.pipe1.surface.x:
            x_collide = True
            pass
        if self.player.surface.x + self.player.surface.w - 15 >= self.pipe2.surface.x:
            x_collide = True
            pass
        if self.player.surface.y + self.player.surface.h <= self.pipe1.surface.y + self.pipe1.surface.h/2 - 20:
            if self.player.surface.y + self.player.surface.h >= self.pipe1.surface.y*2 + self.pipe1.surface.h/2 + 20:
                y_collide = True
                pass
            pass
        if self.player.surface.y + self.player.surface.h <= self.pipe2.surface.y + self.pipe2.surface.h/2 - 20:
            if self.player.surface.y + self.player.surface.h >= self.pipe2.surface.y*2 + self.pipe2.surface.h/2 + 20:
                y_collide = True
                pass
            pass

        if x_collide and y_collide:
            self.init_as_game(None)
        pass

    def scroll_level(self):
        self.background.surface.x -= 1
        self.floor.surface.x -= 2
        self.pipe1.surface.x -= 2
        self.pipe2.surface.x -= 2
        if self.background.surface.x < -700:
            self.background.surface.x = 0
            pass
        if self.floor.surface.x < -578:
            self.floor.surface.x = 0
            pass
        if self.pipe1.surface.x < -50:
            self.pipe1.surface.x = 650
            self.pipe1.surface.y = random.randint(-325, -100)
            pass
        if self.pipe2.surface.x < -50:
            self.pipe2.surface.x = 650
            self.pipe2.surface.y = random.randint(-325, -100)
            pass
        pass
