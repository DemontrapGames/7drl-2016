import libtcodpy as libtcod
import util.config as config
import util.floor as floor
import util.gui as gui

def handle_keys():
    global playerx, playery

    key = libtcod.console_wait_for_keypress(True) #turn based
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    elif key.vk == libtcod.KEY_ESCAPE:
        return True #exit game

    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        playery -= 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        playery += 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        playerx -= 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        playerx += 1

### Initialization and Main Loop ###
libtcod.console_set_custom_font('terminal10x10_gs_tc.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(config.SCREEN_WIDTH, config.SCREEN_HEIGHT, 'The Trap of the 7 lords', False)
libtcod.sys_set_fps(config.LIMIT_FPS)
con = libtcod.console_new(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
panel = libtcod.console_new(config.SCREEN_WIDTH, config.PANEL_HEIGHT)

floor.make_map()

game_msgs = []

gui.message('Welcome', libtcod.red)

playerx = config.SCREEN_WIDTH/2
playery = config.SCREEN_HEIGHT/2

while not libtcod.console_is_window_closed():

    libtcod.console_set_default_foreground(con, libtcod.white)
    libtcod.console_put_char(con, playerx, playery, '@', libtcod.BKGND_NONE)

    libtcod.console_blit(con, 0, 0, config.SCREEN_WIDTH, config.SCREEN_HEIGHT, 0, 0, 0)
    libtcod.console_flush()

    libtcod.console_put_char(con, playerx, playery, ' ', libtcod.BKGND_NONE)

    exit = handle_keys()
    if exit:
        break