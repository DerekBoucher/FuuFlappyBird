# Imports
import sdl2.ext
import sdl2
import sdl2.sdlimage
import ctypes
from bird import bird
from pipe import pipe
from pipe import pipeTopLowBound
from pipe import pipeTopHighBound
from pipe import pipeOffset
from pipe import pipeWidth
from pipe import pipeHeight
from bird import birdWidth
from bird import birdHeight
from floor import floor
from entity import entity
from background import background
from score import score
import time
import random
from title import title

background_img = b"../assets/background.png"


class scene(entity):

    def __init__(self):
        entity.__init__(self)
        self.event = sdl2.SDL_Event()
        self.type = None
        self.entities = None    # List containing all of the scene's entities
        self.background = None
        self.floor = None
        self.pipe1_bot = None
        self.pipe1_top = None
        self.pipe2_bot = None
        self.pipe2_top = None
        self.player = None
        self.index_player = None
        self.score = None
        self.title = None
        self.RequestChange = False
        self.Pause = True
        pass

    def process_events(self):
        if self.type == "game":
            while sdl2.SDL_PollEvent(ctypes.byref(self.event)) != 0:
                if self.event.type == sdl2.SDL_QUIT:
                    self.Running = False
                    break
                if self.event.type == sdl2.SDL_KEYDOWN:
                    if self.event.key.keysym.sym == sdl2.SDLK_SPACE:
                        if not self.player.is_alive():
                            self.player.start()
                            pass
                        self.player.flap()
                    if self.event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                        self.init_as_game(None)
                        self.RequestChange = True
                        pass
                pass
        elif self.type == "menu":
            while sdl2.SDL_PollEvent(ctypes.byref(self.event)) != 0:
                if self.event.type == sdl2.SDL_QUIT:
                    self.Running = False
                    break
                if self.event.type == sdl2.SDL_KEYDOWN:
                    if self.event.key.keysym.sym == sdl2.SDLK_SPACE:
                        self.RequestChange = True
            pass
        pass

    def init_as_game(self, rend):
        if rend is not None:
            self.type = "game"
            self.background = background(rend)
            self.floor = floor(rend)
            self.pipe1_bot = pipe(rend, False)
            self.pipe1_top = pipe(rend, True)
            self.pipe2_bot = pipe(rend, False)
            self.pipe2_top = pipe(rend, True)
            self.pipe1_top.surface.x = 804
            self.pipe1_bot.surface.x = 804
            self.pipe2_top.surface.x = 1130
            self.pipe2_bot.surface.x = 1130
            self.player = bird(rend)
            self.score = score(rend)
            self.entities = [self.background,
                             self.pipe1_bot,
                             self.pipe1_top,
                             self.pipe2_bot,
                             self.pipe2_top,
                             self.floor,
                             self.player,
                             self.score]
            self.index_player = self.entities.index(self.player)
            self.start()
        else:
            self.player.surface.x = 80
            self.player.surface.y = 270
            self.pipe1_top.surface.x = 800
            self.pipe2_top.surface.x = 1130
            self.pipe1_bot.surface.x = 800
            self.pipe2_bot.surface.x = 1130
            self.pipe1_top.surface.y = random.randint(pipeTopLowBound, pipeTopHighBound)
            self.pipe1_bot.surface.y = self.pipe1_top.surface.y + pipeOffset
            self.pipe2_top.surface.y = random.randint(pipeTopLowBound, pipeTopHighBound)
            self.pipe2_bot.surface.y = self.pipe2_top.surface.y + pipeOffset
            self.background.surface.x = 0
            self.background.surface.y = 0
            self.floor.surface.x = 0
            self.score.count = 0
            self.score.update_textures()
        pass

    def init_as_menu(self, rend):
        self.type = "menu"
        self.background = background(rend)
        self.floor = floor(rend)
        self.player = bird(rend)
        self.player.surface.x = 240
        self.title = title(rend)
        self.entities = [
            self.background,
            self.floor,
            self.player,
            self.title
        ]
        self.index_player = self.entities.index(self.player)
        self.start()
        pass

    def run(self):
        self.Running = True
        while self.Running:
            if self.type == "game":
                self.scroll_level()
                self.detect_collisions()
                self.update_score()
                time.sleep(0.00875)
            elif self.type == "menu":
                self.scroll_level()
                time.sleep(0.00875)
                pass
            pass
        pass

    def stop_entities(self):
        for i in self.entities:
            i.stop()
            if i.is_alive():
                i.join()
        self.Running = False

    def update_score(self):
        if self.player.surface.x == self.pipe1_top.surface.x + pipeWidth:
            self.score.increment()
            self.score.update_textures()
        if self.player.surface.x == self.pipe2_top.surface.x + pipeWidth:
            self.score.increment()
            self.score.update_textures()

    def detect_collisions(self):
        x_collide = False
        y_collide = False
        top_pipe = None
        bot_pipe = None

        if (self.pipe1_top.surface.x < self.pipe2_top.surface.x)\
                and (self.pipe1_top.surface.x > self.player.surface.x):
            top_pipe = self.pipe1_top
            bot_pipe = self.pipe1_bot
        else:
            top_pipe = self.pipe2_top
            bot_pipe = self.pipe2_bot

        # Check X Collisions
        for i in range(self.player.surface.x + 30, self.player.surface.x + birdWidth - 20):
            if top_pipe.surface.x < i < top_pipe.surface.x + pipeWidth:
                x_collide = True
                break

        # Check Y Collisions
        for i in range(self.player.surface.y + 15, self.player.surface.y + birdHeight - 10):
            if top_pipe.surface.y < i < top_pipe.surface.y + pipeHeight - 15:
                y_collide = True
                break
            if bot_pipe.surface.y + 15 < i < bot_pipe.surface.y + pipeHeight:
                y_collide = True
                break

        if x_collide and y_collide:
            self.init_as_game(None)

    def scroll_level(self):
        self.background.surface.x -= 1
        self.floor.surface.x -= 2
        if self.background.surface.x < -700:
            self.background.surface.x = 0
            pass
        if self.floor.surface.x < -578:
            self.floor.surface.x = 0
            pass
        if self.type == "game":
            self.pipe1_top.surface.x -= 2
            self.pipe1_bot.surface.x -= 2
            self.pipe2_top.surface.x -= 2
            self.pipe2_bot.surface.x -= 2
            if self.pipe1_top.surface.x < -50:
                self.pipe1_top.surface.x = 650
                self.pipe1_bot.surface.x = 650
                self.pipe1_top.surface.y = random.randint(pipeTopLowBound, pipeTopHighBound)
                self.pipe1_bot.surface.y = self.pipe1_top.surface.y + pipeOffset
                pass
            if self.pipe2_top.surface.x < -50:
                self.pipe2_top.surface.x = 650
                self.pipe2_bot.surface.x = 650
                self.pipe2_top.surface.y = random.randint(pipeTopLowBound, pipeTopHighBound)
                self.pipe2_bot.surface.y = self.pipe2_top.surface.y + pipeOffset
            pass
        pass
