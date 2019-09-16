# Imports
import ctypes
import sdl2
import sdl2.ext
from sdl2.sdlimage import IMG_Load
from entity import entity
from time import sleep
import random

pipe_path = b"../assets/pipe.png"

class Pipe(entity):
    def __init__(self, rend):
        entity.__init__(self)
        self.texture = sdl2.SDL_CreateTextureFromSurface(rend, IMG_Load(pipe_path))
        self.surface = sdl2.SDL_Rect(650, 0, 50, 900)
        self.surface.y = random.randint(-325, -100)
        pass