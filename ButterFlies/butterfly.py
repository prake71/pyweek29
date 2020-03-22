import pgzero, pgzrun, pygame
import math, sys, random
from pygame.math import Vector2

if sys.version_info < (3,5):
    print("This game requires at least Python 3.5. Please download from www.python.org")
    sys.exit()

WIDTH = 800
HEIGHT = 480
TITLE = "ButterFly"

HALF_WIDTH = WIDTH / 2

pgzrun.go()

