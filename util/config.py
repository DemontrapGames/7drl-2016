import libtcodpy as libtcod

player = None

currentFloorNumber = 0 # the current floor that the player is on
floors = [] # list to hold all of the floors

# setting up some vars used by and for libtcod
#
### Code for map generation ###
MAP_WIDTH = 80
MAP_HEIGHT = 45

color_dark_wall = libtcod.Color(0, 0, 100)
color_dark_ground = libtcod.Color(50, 50, 150)

### Screen Size for libtcod ###
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

LIMIT_FPS = 20
