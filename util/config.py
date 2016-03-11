import libtcodpy as libtcod

player = None

currentFloorNumber = 0 # the current floor that the player is on
floors = [] # list to hold all of the floors

# setting up some vars used by and for libtcod
#
### Code for map generation ###
MAP_WIDTH = 80
MAP_HEIGHT = 43

color_dark_wall = libtcod.Color(0, 0, 100)
color_dark_ground = libtcod.Color(50, 50, 150)

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

### Screen Size for libtcod ###
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

LIMIT_FPS = 20

### GUI ###
BAR_WIDTH = 20
PANEL_HEIGHT = 7
PANEL_Y = SCREEN_HEIGHT - PANEL_HEIGHT

MSG_X = BAR_WIDTH + 2
MSG_WIDTH = SCREEN_WIDTH - BAR_WIDTH - 2
MSG_HEIGHT = PANEL_HEIGHT - 1
