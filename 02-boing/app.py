import pgzero, pgzrun, pygame
import sys, math, random
from enum import Enum

from constants import (
    WIDTH,
    HEIGHT,
    TITLE,
    HALF_HEIGHT,
    HALF_WIDTH,
    PLAYER_SPEED,
    MAX_AI_SPEED
)


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


class Bat(Actor):
    def __init__(self, player=None, move_func=None):
        x = 40
        y = HALF_HEIGHT
        super().__init__("blank", (x, y))

    def update(self):
        self.image = "bat00"

    def ai(self):
        pass



class Game:
    def __init__(self, controls=(None, None)):
        self.bat = Bat()

    def update(self):
        self.bat.update()

    def draw(self):
        screen.blit("table", (0, 0))

        self.bat.draw()

    def play_sound(self, name, count=1):
        pass


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

    if state == State.MENU:
        if space_pressed:
            state = State.PLAY
        else:
            if keyboard.up:
                print("++++++")
                print("Keyboard up")
                print("++++++")

                sounds.up.play()
                num_players = 1

            elif keyboard.down:
                print("++++++")
                print("Keyboard down")
                print("++++++")

                sounds.down.play()
                num_players = 2

    elif state == State.PLAY:
        game.update()


def draw():
    game.draw()

    if state == State.MENU:
        menu_image = "menu" + str(num_players - 1)
        screen.blit(menu_image, (0, 0))

    elif state == State.GAME_OVER:
        screen.blit("over", (0, 0))

try:
    pygame.mixer.quit()
    pygame.mixer.init()

    music.play("theme")
    music.set_volume(0.3)
except:
    print("Failed playing music")
    pass



state = State.MENU
game = Game()

pgzrun.go()


