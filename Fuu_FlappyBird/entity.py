# Set SDL2 DLL Path
import os
os.environ["PYSDL2_DLL_PATH"] = os.getcwd()+"\\..\\lib"

# Imports
import sdl2
import sdl2.ext
import sdl2.sdlimage
import sys
import ctypes
from threading import Thread
import threading

class entity(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.texture = 0
        self.surface = 0
        self.Running = False
        pass

    def Render(self, rend):
        sdl2.SDL_RenderCopy(rend, self.texture, None, ctypes.byref(self.surface))
        pass

    def stop(self):
        self.Running = False
        pass
