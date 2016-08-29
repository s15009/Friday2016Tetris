import pyglet

import gametypes


WIDTH = 800
HEIGHT = 600
BOARD_X = 250
BOARD_Y = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 25
SET_QUEUE = 3

window = pyglet.window.Window(WIDTH, HEIGHT)
window.set_vsync(False)

###### load resources ######
pyglet.resource.path = ['res']
backgroundImage = pyglet.resource.image('background.jpg')
blocksImage = pyglet.resource.image('block2.png')
BoradImage = pyglet.resource.image('board2.png')
gametypes.TetrominoType.class_init(blocksImage, BLOCK_SIZE)

###### init game state ######
queue = gametypes.NextTetrominoQueue(600, 300, BLOCK_SIZE, 2)
board = gametypes.Board(BOARD_X, BOARD_Y, GRID_WIDTH, GRID_HEIGHT, BLOCK_SIZE, BoradImage, queue)
infoDisplay = gametypes.InfoDisplay(window)
input = gametypes.Input()
game = gametypes.Game(board, infoDisplay, input, backgroundImage)


@window.event
def on_key_press(symbol, modifiers):
    input.process_keypress(symbol, modifiers)


@window.event
def on_text_motion(motion):
    input.process_text_motion(motion)


@window.event
def on_draw():
    game.draw()


def update(dt):
    game.update()


pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()
