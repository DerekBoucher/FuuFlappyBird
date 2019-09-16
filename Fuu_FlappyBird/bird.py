# Imports
import sdl2
import sdl2.ext
from sdl2.sdlimage import IMG_Load
from entity import entity
from time import sleep

image_path = b"../assets/bird.png"


class Bird(entity):

    def __init__(self, rend):
        entity.__init__(self)
        self.texture = sdl2.SDL_CreateTextureFromSurface(rend, IMG_Load(image_path))
        self.surface = sdl2.SDL_Rect(80, 270, 100, 60)
        self.acc = 7.0
        self.vel = 0.0
        pass

    def run(self):
        self.Running = True
        while self.Running:
            self.vel += self.acc * 0.0125
            self.surface.y += int(self.vel)
            if self.surface.y >= 435:
                self.surface.y = 435
                self.vel = 0.0
            if self.surface.y <= -5:
                self.surface.y = -5
                self.vel = 1.0
            sleep(0.0125)
            pass
        pass

    def flap(self):
        self.vel -= 2.5
