from entity import entity
import sdl2.ext
import sdl2
from sdl2.sdlimage import IMG_Load

title_img = b"../assets/title.png"


class title(entity):

    def __init__(self, rend):
        entity.__init__(self)
        self.texture = sdl2.SDL_CreateTextureFromSurface(rend, IMG_Load(title_img))
        self.surface = sdl2.SDL_Rect(120, 50, 370, 133)
        self.Running = False
