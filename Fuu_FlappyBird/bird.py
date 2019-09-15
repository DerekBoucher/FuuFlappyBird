# Set SDL2 DLL Path
import os
os.environ["PYSDL2_DLL_PATH"] = os.getcwd()+"\\..\\lib"

# Imports
import sdl2
import sdl2.ext
from sdl2.sdlimage import IMG_Load
import sys
import ctypes
from entity import entity
from time import sleep

image_path = b"../assets/bird.png"

class bird(entity):

    def __init__(self, rend):
        entity.__init__(self)
        self.texture = sdl2.SDL_CreateTextureFromSurface(rend, IMG_Load(image_path))
        self.surface = sdl2.SDL_Rect()
        self.surface.x = 80
        self.surface.y = 270
        self.surface.w = 100
        self.surface.h = 60
        self.acc = 5.0
        self.vel = 0.0
        pass

    def run(self):
        self.Running = True
        while self.Running:
            self.vel        += self.acc * 0.01
            self.surface.y  += int(self.vel)
            sleep(0.01)
            pass
        pass


