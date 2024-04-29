
from py.frontend.PYGAMEwindow import PYGAMEwindow as Window
from py.api import *
import math

RADIUS = 10
SPEED = 10

class Player():
    pass

player = Player()
player.x = 50
player.y = 150
player.speed_x = 0
player.speed_y = 0

def draw_block(window, x, y):
    gui_draw_rect(window, x + 1, y + 1, x + 99, y + 99, Color(0, 0, 255))
    gui_draw_rect(window, x + 11, y + 11, x + 99 - 10, y + 99 - 10, Color(0, 0, 150))
    
def keyboard(window, keycode, flag):
    global player
    if keycode == KEY_W:
        if flag:
            player.speed_y -= SPEED
        else:
            player.speed_y += SPEED
    elif keycode == KEY_S:
        if flag:
            player.speed_y += SPEED
        else:
            player.speed_y -= SPEED
    elif keycode == KEY_A:
        if flag:
            player.speed_x -= SPEED
        else:
            player.speed_x += SPEED
    elif keycode == KEY_D:
        if flag:
            player.speed_x += SPEED
        else:
            player.speed_x -= SPEED

def collide(x, y):
    new_x = x + player.speed_x
    new_y = y + player.speed_y

    row = int(new_y // 100)
    col = int(new_x // 100)
    
    if map[row][col] == "b":
        return 'yes'
    else:
        return 'no'

window = Window(3000, 1200)

gui_create(window)

map = ["bbbbbbbbbbbbbbbbbbbbbb",
       "  bbb     bbb       bb",
       "b b bb  b  b     b  bb",
       "b       b  b     b    ",
       "b  bbb  b  b     bbbbb",
       "bb  bb  b            b",
       "bbbbbbbbbbbbbbbbbbbbbb"]

for row in range(len(map)):
    for col in range(len(map[row])):
        if map[row][col] == "b":
            draw_block(window, col * 100, row * 100)

gui_key_hook(window, keyboard)

while True:
    gui_draw_circle(window, player.x, player.y, RADIUS, COLOR_BLACK)
    
    
    a = RADIUS / math.sqrt(2)
    if collide(player.x + RADIUS, player.y) == 'no' and \
       collide(player.x - RADIUS, player.y) == 'no' and \
       collide(player.x, player.y - RADIUS) == 'no' and \
       collide(player.x, player.y + RADIUS) == 'no' and \
       collide(player.x - a, player.y + a) == 'no' and \
       collide(player.x - a, player.y - a) == 'no' and \
       collide(player.x + a, player.y - a) == 'no' and \
       collide(player.x + a, player.y + a) == 'no' :
        player.x += player.speed_x
        player.y += player.speed_y


    gui_draw_circle(window, player.x, player.y, RADIUS, COLOR_GREEN)
    gui_draw(window)


