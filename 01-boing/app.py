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


def normalize(x, y):
    length = math.hypot(x, y)
    return (x / length, y / length)



def sign(x):
    return -1 if x < 0 else 1


class Impact(Actor):
    def __init__(self, pos):
        super().__init__("blank", pos)
        self.time = 0

    def update(self):
        self.image = "impact" + str(self.time // 2)
        self.time += 1


class Ball(Actor):
    def __init__(self, dx):
        super().__init__("ball", (0, 0))
        self.x, self.y = HALF_WIDTH, HALF_HEIGHT
        self.dx, self.dy = dx, 0
        self.speed = 5

    def update(self):
        for i in range(self.speed):
            original_x = self.x
            self.x += self.dx
            self.y += self.dy

       # Needs to implement game object before moving on 


    def out(self):
        return


class Bat(Actor):
    def __init__(self, player, move_func=None):
        x = 40 if player == 0 else 760
        y = HALF_HEIGHT
        super().__init__("blank", (x, y))

        self.player = player
        self.score = 0

        if move_func != None:
            self.move_func = move_func
        else:
            self.move_func = self.ai

        self.timer = 0

    def update(self):
        return

    def ai(self):
        return


class Game:
    def __init__(self, controls=(None, None)):
        self.bats = [Bat(0, controls[0]), Bat(1, controls[1])]
        self.ball = Ball(-1)
        self.impacts = []
        self.ai_offset = 0

    def update(self):
        return

    def draw(self):
        return

    def play_sound(self):
        return


def p1_controls():
    return


def p2_controls():
    return


class State(Enum):
    MENU = 1
    PLAY = 2
    GAME_OVER = 3


num_players = 1
space_down = False


def update():
    return


def draw():
    return


try:
    pygame.mixer.quit()
    pygame.mixer.init()

    music.play("theme")
    music.set_volume(0.3)
except:
    print("Failed playing music")
    pass



state = State.MENU

#pgzrun.go()


