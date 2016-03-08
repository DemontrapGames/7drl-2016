MAP_WIDTH = 80
MAP_HEIGHT = 45

color_dark_wall = libtcod.Color(0, 0, 100)
color_dark_ground = libtcod.Color(50, 50, 150)

class Tile:
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked

        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight