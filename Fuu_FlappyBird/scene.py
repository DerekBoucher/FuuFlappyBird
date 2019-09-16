# Imports
import sdl2.ext
import sdl2
import ctypes
from bird import Bird
from pipe import Pipe
from entity import entity
from sdl2.sdlimage import IMG_Load
import time
import random

background_img = b"../assets/background.png"
floor_img = b"../assets/floor.png"


class scene(entity):

    def __init__(self):
        entity.__init__(self)
        self.event = sdl2.SDL_Event()
        self.type = None
        self.entities = None
        pass

    def process_events(self):
        if self.type == "game":
            while sdl2.SDL_PollEvent(ctypes.byref(self.event)) != 0:
                if self.event.type == sdl2.SDL_QUIT:
                    self.stop_entities()
                    break
                if self.event.type == sdl2.SDL_KEYDOWN:
                    if self.event.key.keysym.sym == sdl2.SDLK_SPACE:
                        if not self.entities[4].is_alive():
                            self.entities[4].start()
                            pass
                        self.entities[4].flap()
                        pass
                pass
        if self.type == "menu":
            pass
        pass

    def init_as_game(self, rend):
        self.type = "game"
        self.texture = sdl2.SDL_CreateTextureFromSurface(rend, IMG_Load(background_img))
        self.surface = sdl2.SDL_Rect(0, 0, 1575, 500)
        self.floor = entity()
        self.pipe1 = Pipe(rend)
        self.pipe2 = Pipe(rend)
        self.pipe2.surface.x = 1000
        self.floor.texture = sdl2.SDL_CreateTextureFromSurface(rend, IMG_Load(floor_img))
        self.floor.surface = sdl2.SDL_Rect(0, 490, 1200, 150)
        player = Bird(rend)
        self.entities = [self, self.pipe1, self.pipe2, self.floor, player]
        self.start()
        pass

    def init_as_menu(self, rend):
        self.type = "menu"
        pass

    def run(self):
        self.Running = True
        while self.Running:
            if self.type == "game":
                self.surface.x -= 1
                self.floor.surface.x -= 2
                self.pipe1.surface.x -= 2
                self.pipe2.surface.x -= 2
                if self.surface.x < -700:
                    self.surface.x = 0
                    pass
                if self.floor.surface.x < -578:
                    self.floor.surface.x = 0
                    pass
                if self.pipe1.surface.x < -50:
                    self.pipe1.surface.x = 650
                    self.pipe1.surface.y = random.randint(-325, -100)
                if self.pipe2.surface.x < -50:
                    self.pipe2.surface.x = 650
                    self.pipe2.surface.y = random.randint(-325, -100)
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
