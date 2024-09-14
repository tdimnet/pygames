import pgzero, pgzrun, pygame
import sys, math,random
from enum import Enum


if sys.version_info < (3, 5):
    print("This game requires at least version 3.5 for Python.")
    sys.exit()
else:
    print("Version for Python is ok")


pgzero_version = [int(s) if s.isnumeric() else s for s in
                  pgzero.__version__.split('.')]


if pgzero_version < [1, 2]:
    print("This game requires at least version 1.2 of Pygame Zero.")
    sys.exit()
else:
    print("Pygame Zero is ok")


print("Let's ready to start the game")


WIDTH = 800
HEIGHT = 480
TITLE = "Boing!"

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PLAYER_SPEED = 6
MAX_AI_SPEED = 6


class State(Enum):
    MENU = 1
    PLAY = 2
    GAME_OVER = 3


num_players = 1
space_down = False


def update():
    global state, num_players, space_down
    space_pressed = False

    if keyboard.space and not space_down:
        space_pressed = True

    space_down = keyboard.space

    print("=====")
    print("Update has been called")
    print("=====")
    print("=====")
    print("=====")


def draw():

    print("=====")
    print("Draw has been called")
    print("=====")
    print("=====")
    print("=====")

try:
    pygame.mixer.quit()
    pygame.mixer.init()

    music.play("theme")
    music.set_volume(0.3)
except:
    print("Failed playing music")
    pass



state = State.MENU

pgzrun.go()


