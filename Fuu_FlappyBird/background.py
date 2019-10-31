# Imports
import sdl2
import sdl2.ext
from sdl2.sdlimage import IMG_Load
from entity import entity

background_img = b"../assets/background.png"


class background(entity):
    def __init__(self, rend):
        entity.__init__(self)
        self.texture = sdl2.SDL_CreateTextureFromSurface(rend, IMG_Load(background_img))
        self.surface = sdl2.SDL_Rect(0, 0, 1575, 500)
        pass
