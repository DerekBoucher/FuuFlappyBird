# Imports
import sdl2
import sdl2.ext
import sdl2.sdlimage
import ctypes
from threading import Thread


class entity(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.texture = 0
        self.surface = 0
        self.Running = False
        self.isScore = False
        pass

    def render(self, rend):
        if self.isScore:
            sdl2.SDL_RenderCopy(rend, self.texture[0], None, ctypes.byref(self.surface0))
            sdl2.SDL_RenderCopy(rend, self.texture[1], None, ctypes.byref(self.surface1))
            sdl2.SDL_RenderCopy(rend, self.texture[2], None, ctypes.byref(self.surface2))
        else:
            sdl2.SDL_RenderCopy(rend, self.texture, None, ctypes.byref(self.surface))
        pass

    def stop(self):
        self.Running = False
        pass
