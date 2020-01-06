# Imports
import sdl2
import sdl2.ext
from sdl2.sdlimage import IMG_Load
from entity import entity

pipe_path = b"../assets/pipe.png"
pipe_path_inv = b"../assets/pipe_inv.png"
pipeTopLowBound = -275
pipeTopHighBound = -75
pipeOffset = 450
pipeBaseX = 300
pipeWidth = 50
pipeHeight = 375


class pipe(entity):
    def __init__(self, rend, inv):
        entity.__init__(self)
        if inv:
            self.texture = sdl2.SDL_CreateTextureFromSurface(rend, IMG_Load(pipe_path_inv))
            self.surface = sdl2.SDL_Rect(pipeBaseX, -175, pipeWidth, pipeHeight)
        else:
            self.texture = sdl2.SDL_CreateTextureFromSurface(rend, IMG_Load(pipe_path))
            self.surface = sdl2.SDL_Rect(pipeBaseX, 275, pipeWidth, pipeHeight)
