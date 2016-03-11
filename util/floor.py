import libtcodpy as libtcod
import util.config as config

class Tile:
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked

        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight

class Rect:
    #a rectangle on the map. used to characterize a room.
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

def create_room(room):
    global map
    #go through the tiles in the rectangle and make them passable
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            map[x][y].blocked = False
            map[x][y].block_sight = False

def make_map():
    global map

    #fill map with "unblocked" tiles
    map = [[ Tile(False)
        for y in range(config.MAP_HEIGHT) ]
            for x in range(config.MAP_WIDTH) ]

    room1 = Rect(20, 15, 10, 15)
    room2 = Rect(50, 15, 10, 15)
    create_room(room1)
    create_room(room2)

    create_h_tunnel(25, 55, 23)

def create_h_tunnel(x1, x2, y):
    global map
    for x in range(min(x1, x2), max(x1, x2) + 1):
        map[x][y].blocked = False
        map[x][y].block_sight = False

def create_v_tunnel(y1, y2, x):
    global map
    #vertical tunnel
    for y in range(min(y1, y2), max(y1, y2) + 1):
        map[x][y].blocked = False
        map[x][y].block_sight = False

con = libtcod.console_new(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)

def render_all():
    global color_light_wall
    global color_light_ground

    for y in range(config.MAP_HEIGHT):
        for x in range(config.MAP_WIDTH):
            wall = map[x][y].block_sight
            if wall:
                libtcod.console_set_char_background(con, x, y, config.color_dark_wall, libtcod.BKGND_SET )
            else:
                libtcod.console_set_char_background(con, x, y, config.color_dark_ground, libtcod.BKGND_SET )

    y = 1
    for (line, color) in game_msgs:
        libtcod.console_set_default_foreground(panel, color)
        libtcod.console_print_ex(panel, MSG_X, y, libtcod.BKGND_NONE, libtcod.LEFT, line)
        y += 1