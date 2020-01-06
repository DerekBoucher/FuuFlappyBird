# Imports
import sdl2.ext
import sdl2


# Main Rendering Function, performs rendering using painter's algorithm,
# where the farthest element (0th element in list) is rendered first and everything
# else over it.
def perform_rendering(rend, entities=[]):
    for entity in entities:
        entity.render(rend)
        pass
    sdl2.SDL_RenderPresent(rend)
    pass
