# Imports
import sdl2.ext
import sdl2

# Main Rendering Function, performs rendering using painter's algorithm,
# where the farthest element (0th element in list) is rendered fisrt and everything
# else over it.
def Perform_Rendering(rend, entities = []):

    for entity in entities:
        entity.Render(rend)
        pass
    
    sdl2.SDL_RenderPresent(rend)
    pass

