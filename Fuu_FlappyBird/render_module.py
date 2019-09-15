# Set SDL2 DLL Path
import os
os.environ["PYSDL2_DLL_PATH"] = os.getcwd()+"\\..\\lib"

# Imports
import sys
import sdl2.ext
import sdl2
import ctypes
import bird

# Main Rendering Function, performs rendering using painter's algorithm,
# where the farthest element (0th element in list) is rendered fisrt and everything
# else over it.
def Perform_Rendering(rend, entities = []):

    for entity in entities:
        entity.Render(rend)
        pass
    
    sdl2.SDL_RenderPresent(rend)
    pass

