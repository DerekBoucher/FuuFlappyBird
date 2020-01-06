# Set SDL2 DLL Path
import os
import platform

if platform.system() == "Darwin":
    os.environ["PYSDL2_DLL_PATH"] = os.getcwd() + "/lib/MacOS"
    pass

if platform.system() == "Windows":
    os.environ["PYSDL2_DLL_PATH"] = os.getcwd() + "\\..\\lib\\Windows"
    pass

# Imports
import sdl2
from render_module import perform_rendering
from scene import scene

# Initialize Subsystems
sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)

# Window Parameters
winName = b"Fuu Flappy Bird"
win_width = 600
win_height = 600
window = sdl2.SDL_CreateWindow(winName,
                               sdl2.SDL_WINDOWPOS_CENTERED,
                               sdl2.SDL_WINDOWPOS_CENTERED,
                               win_width,
                               win_height,
                               sdl2.SDL_WINDOW_SHOWN)
renderer = sdl2.SDL_CreateRenderer(window,
                                   -1,
                                   sdl2.SDL_RENDERER_ACCELERATED | sdl2.SDL_RENDERER_PRESENTVSYNC)

# Instantiate Scenes
gameScene = scene()
gameScene.init_as_game(renderer)
menuScene = scene()
menuScene.init_as_menu(renderer)
sceneList = [gameScene, menuScene]

# Scene Indexes
game_scene_index = 0
menu_scene_index = 1
current_scene_index = menu_scene_index
sceneList[current_scene_index].Pause = False

# Clear Screen to Black
sdl2.SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255)
sdl2.SDL_RenderClear(renderer)

# Main Game Loop
while sceneList[current_scene_index].Running:
    # Process Events
    sceneList[current_scene_index].process_events()

    if sceneList[current_scene_index].RequestChange:
        sceneList[current_scene_index].RequestChange = False
        if current_scene_index == menu_scene_index:
            current_scene_index = game_scene_index
            sceneList[current_scene_index].init_as_game(None)
        else:
            current_scene_index = menu_scene_index

    # Render Graphics
    perform_rendering(renderer, sceneList[current_scene_index].entities)
    pass

# Clean up
for scene in sceneList:
    scene.stop_entities()
sdl2.SDL_DestroyRenderer(renderer)
sdl2.SDL_DestroyWindow(window)
sdl2.SDL_Quit()
