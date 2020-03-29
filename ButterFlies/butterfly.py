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

GRAVITY = 0.3
FLAP_STRENGTH = 6.5
SPEED = 3
AIR_RESISTANCE = 0.29

butterfly = Actor('bf001.png', (75,200))
butterfly.vy = 0
butterfly.images = ['bf001.png', 'bf002.png', 'bf003.png', 'bf004.png', 'bf005.png', 'bf006.png', 'bf007.png', 'bf008.png', 'bf009.png', 'bf010.png', 'bf011.png', 'bf012.png', 'bf013.png', 'bf014.png', 'bf015.png' ]
butterfly.frame = 0
butterfly.delay = 3
butterfly.pause = butterfly.delay


#samen = Actor('samen.png', (500, 0))
samen = Actor('samen_tb.png', (500,10))
samen.images = ['samen_tb.png', 'samen_mirror_tb.png']
samen.vy = 0
samen.frame = 0
samen.delay = 10
samen.pause = samen.delay


class Flower():
    def __init__(self, xpos):
        self.pos = Vector2(xpos, HEIGHT)
        print(self.pos)
        self.to_pos = Vector2(xpos, HEIGHT)
        self.delay = 10 # grow every 10th frame
        self.pause = self.delay
        self.max_length = 100

        print("Constructor")


    def update(self):
        print("update")
        if (self.pos.distance_to(self.to_pos)) <= 100:
            self.pause -= 1
            print("pause", self.pause)
            if self.pause <= 0:
                self.pause = self.delay
                self.to_pos += Vector2(0, -1)
        print("in updated pos:",self.pos)


    def draw_circle(self):
        pass


    def draw(self, screen):
        screen.draw.line(self.pos, self.to_pos, (1,1,1))
        print("in draw")
        print(self.pos, self.to_pos)


#samen.images[0].set_colorkey((1,1,1))
#samen.image = samen.images[0]

def update_samen():
    if samen.y < HEIGHT:
        samen.y += GRAVITY
    samen.pause -= 1
    if samen.pause <= 0:
        samen.pause = samen.delay
        if samen.frame == 0:
            samen.frame = 1
        elif samen.frame == 1:
            samen.frame = 0
        samen.image = samen.images[samen.frame]


def update_butterfly():
    uy = butterfly.vy
    butterfly.vy += GRAVITY
    butterfly.y += (uy + butterfly.vy) / 2
    if keyboard.left:
        butterfly.x -= 1 * SPEED
    if keyboard.right:
        butterfly.x += 1 * SPEED

    butterfly.pause -= 1
    if butterfly.pause <= 0:
        butterfly.pause = butterfly.delay
        butterfly.frame += 1
        if butterfly.frame > 14:
            butterfly.frame = 0
    #print("butterfly.vy = ", butterfly.vy)
    if butterfly.vy < -3:
        butterfly.image = butterfly.images[butterfly.frame]
    else:
        butterfly.image = butterfly.images[butterfly.frame]
    check_bounds(butterfly)

def check_bounds(actor):
    if actor.x > WIDTH:
        actor.x = WIDTH
    if actor.x < 0:
        actor.x = 0
    if actor.y > HEIGHT:
        actor.y = HEIGHT
    if actor.y < 0:
        actor.y = 0



def on_key_down(key):
    print(key)
    if key == keys.F:
        butterfly.vy = -FLAP_STRENGTH
        butterfly_flap()


def apply_force(Actor: object, dir: object, dist) -> object:
    strength = (1000 / dist)
    print("strength:", strength)
    samen.x += (dir * strength) * 3


def butterfly_flap():
    direction = 0
    if int(butterfly.y) in range(int(samen.y - 50), int(samen.y + 50)):
        if butterfly.x < samen.x:
            direction = 1
        elif butterfly.x > samen.x:
            direction = -1
        butv = Vector2(butterfly.x, butterfly.y)
        samv = Vector2(samen.x, samen.y)

        dist = butv.distance_to(samv)
        print(dist)
        apply_force(samen, direction, dist)

def update():
    update_butterfly()
    update_samen()
    flower.update()

def draw():
    screen.clear()
    screen.fill((126,200,80))
    #screen.clear()
    butterfly.draw()
    samen.draw()
    flower.draw(screen)

flower = Flower(400)

pgzrun.go()

