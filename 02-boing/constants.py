from enum import Enum

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


