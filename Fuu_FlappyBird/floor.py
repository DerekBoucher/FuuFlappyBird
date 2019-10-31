# Imports
import sdl2
import sdl2.ext
from sdl2.sdlimage import IMG_Load
from entity import entity

floor_img = b"../assets/floor.png"


class floor(entity):
    def __init__(self, rend):
        entity.__init__(self)
        self.texture = sdl2.SDL_CreateTextureFromSurface(rend, IMG_Load(floor_img))
        self.surface = sdl2.SDL_Rect(0, 490, 1200, 150)
        pass
