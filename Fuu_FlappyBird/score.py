from entity import entity
import sdl2.ext
import sdl2
from sdl2.sdlimage import IMG_Load

img0 = b"../assets/0.png"
img1 = b"../assets/1.png"
img2 = b"../assets/2.png"
img3 = b"../assets/3.png"
img4 = b"../assets/4.png"
img5 = b"../assets/5.png"
img6 = b"../assets/6.png"
img7 = b"../assets/7.png"
img8 = b"../assets/8.png"
img9 = b"../assets/9.png"
blank = b"../assets/blank.png"


class score(entity):

    def __init__(self, rend):
        entity.__init__(self)
        self.texture = [sdl2.SDL_CreateTextureFromSurface(rend, IMG_Load(img0)),
                        sdl2.SDL_CreateTextureFromSurface(rend, IMG_Load(blank)),
                        sdl2.SDL_CreateTextureFromSurface(rend, IMG_Load(blank))]
        self.isScore = True
        self.surface0 = sdl2.SDL_Rect(300, 25, 97-70, 129-80)
        self.surface1 = sdl2.SDL_Rect(300 - 40, 25, 97-70, 129-80)
        self.surface2 = sdl2.SDL_Rect(300 - (2 * 40), 25, 97-70, 129-80)
        self.count = 0
        self.rend = rend
        self.update_textures()

    def update_textures(self):
        if self.count % 10 == 0:
            self.texture[0] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img0))
        elif self.count % 10 == 1:
            self.texture[0] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img1))
        elif self.count % 10 == 2:
            self.texture[0] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img2))
        elif self.count % 10 == 3:
            self.texture[0] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img3))
        elif self.count % 10 == 4:
            self.texture[0] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img4))
        elif self.count % 10 == 5:
            self.texture[0] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img5))
        elif self.count % 10 == 6:
            self.texture[0] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img6))
        elif self.count % 10 == 7:
            self.texture[0] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img7))
        elif self.count % 10 == 8:
            self.texture[0] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img8))
        elif self.count % 10 == 9:
            self.texture[0] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img9))

        if self.count / 10 == 0:
            self.texture[1] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(blank))
        elif self.count / 10 == 1:
            self.texture[1] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img1))
        elif self.count / 10 == 2:
            self.texture[1] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img2))
        elif self.count / 10 == 3:
            self.texture[1] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img3))
        elif self.count / 10 == 4:
            self.texture[1] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img4))
        elif self.count / 10 == 5:
            self.texture[1] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img5))
        elif self.count / 10 == 6:
            self.texture[1] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img6))
        elif self.count / 10 == 7:
            self.texture[1] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img7))
        elif self.count / 10 == 8:
            self.texture[1] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img8))
        elif self.count / 10 == 9:
            self.texture[1] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img9))

        if self.count / 100 == 0:
            self.texture[2] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(blank))
        elif self.count / 100 == 1:
            self.texture[2] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img1))
        elif self.count / 100 == 2:
            self.texture[2] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img2))
        elif self.count / 100 == 3:
            self.texture[2] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img3))
        elif self.count / 100 == 4:
            self.texture[2] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img4))
        elif self.count / 100 == 5:
            self.texture[2] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img5))
        elif self.count / 100 == 6:
            self.texture[2] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img6))
        elif self.count / 100 == 7:
            self.texture[2] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img7))
        elif self.count / 100 == 8:
            self.texture[2] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img8))
        elif self.count / 100 == 9:
            self.texture[2] = sdl2.SDL_CreateTextureFromSurface(self.rend, IMG_Load(img9))

    def increment(self):
        self.count += 1
