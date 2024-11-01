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
    MAX_AI_SPEED,
    State
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


# For now I put p1 controls here
def p1_controls():
    move = 0

    if keyboard.z or keyboard.down:
        move = PLAYER_SPEED
    elif keyboard.a or keyboard.up:
        move -= PLAYER_SPEED

    return move


class Ball(Actor):
    def __init__(self):
        super().__init__("ball", (0, 0))
        self.x = HALF_WIDTH
        self.y = HALF_HEIGHT
        self.dx, self.dy = 5, 2
        self.speed = 1


    def update(self):
        for i in range(self.speed):
            original_x = self.x
            self.x += self.dx
            self.y += self.dy

            # if abs(self.x - HALF_WIDTH) > 344:
            if abs(self.x - HALF_WIDTH) > 380:
                self.dx = -self.dx
                self.x += self.dx

            if abs(self.y - HALF_HEIGHT) > 220:
                self.dy = -self.dy
                self.y += self.dy



class Bat(Actor):
    def __init__(self, player=None, move_func=p1_controls):
        x = 40
        y = HALF_HEIGHT
        super().__init__("bat00", (x, y))
        self.move_func = move_func

    def update(self):
        y_movement = self.move_func()
        self.y = min(400, max(80, self.y + y_movement))

        # print(self.y)

    def ai(self):
        pass



class Game:
    def __init__(self, controls=(None, None)):
        self.bat = Bat()
        self.ball = Ball()

    def update(self):
        self.bat.update()
        self.ball.update()

    def draw(self):
        screen.blit("table", (0, 0))

        # self.bat.draw()
        self.ball.draw()

    def play_sound(self, name, count=1):
        pass


num_players = 1
space_down = False



def p2_controls():
    pass


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
    pass
    # pygame.mixer.quit()
    # pygame.mixer.init()

    # music.play("theme")
    # music.set_volume(0.1)
except:
    print("Failed playing music")
    pass



state = State.MENU
game = Game()

pgzrun.go()


