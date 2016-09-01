import random
from collections import deque

import pyglet


class TetrominoType(object):
    TYPES = tuple()

    def __init__(self, block_image, local_block_coords_by_orientation):
        self.blockImage = block_image
        self.localBlockCoordsByOrientation = local_block_coords_by_orientation

    @staticmethod
    def class_init(block_image, block_size):
        cyan = block_image.get_region(x=0, y=0, width=block_size,
                                      height=block_size)
        yellow = block_image.get_region(x=block_size, y=0, width=block_size,
                                        height=block_size)
        green = block_image.get_region(x=block_size * 2, y=0, width=block_size,
                                       height=block_size)
        red = block_image.get_region(x=block_size * 3, y=0, width=block_size,
                                     height=block_size)
        blue = block_image.get_region(x=block_size * 4, y=0, width=block_size,
                                      height=block_size)
        orange = block_image.get_region(x=block_size * 5, y=0,
                                        width=block_size, height=block_size)
        purple = block_image.get_region(x=block_size * 6, y=0,
                                        width=block_size, height=block_size)

        TetrominoType.TYPES = [
            # type I
            TetrominoType(cyan,
                          {
                              Tetromino.RIGHT: [(0, 1), (1, 1), (2, 1),
                                                (3, 1)],
                              Tetromino.DOWN: [(1, 0), (1, 1), (1, 2), (1, 3)],
                              Tetromino.LEFT: [(0, 2), (1, 2), (2, 2), (3, 2)],
                              Tetromino.UP: [(2, 0), (2, 1), (2, 2), (2, 3)],
                          }
                          ),
            # type O
            TetrominoType(yellow,
                          {
                              Tetromino.RIGHT: [(0, 0), (0, 1), (1, 0),
                                                (1, 1)],
                              Tetromino.DOWN: [(0, 0), (0, 1), (1, 0), (1, 1)],
                              Tetromino.LEFT: [(0, 0), (0, 1), (1, 0), (1, 1)],
                              Tetromino.UP: [(0, 0), (0, 1), (1, 0), (1, 1)],
                          }
                          ),
            # type S
            TetrominoType(green,
                          {
                              Tetromino.RIGHT: [(0, 0), (1, 0), (1, 1),
                                                (2, 1)],
                              Tetromino.DOWN: [(0, 1), (0, 2), (1, 1), (1, 0)],
                              Tetromino.LEFT: [(0, 0), (1, 0), (1, 1), (2, 1)],
                              Tetromino.UP: [(0, 1), (0, 2), (1, 1), (1, 0)],
                          }
                          ),
            # type Z
            TetrominoType(red,
                          {
                              Tetromino.RIGHT: [(1, 1), (0, 1), (1, 0),
                                                (2, 0)],
                              Tetromino.DOWN: [(1, 1), (1, 0), (2, 1), (2, 2)],
                              Tetromino.LEFT: [(1, 1), (0, 1), (1, 0), (2, 0)],
                              Tetromino.UP: [(1, 1), (1, 0), (2, 1), (2, 2)],
                          }
                          ),
            # type J
            TetrominoType(blue,
                          {
                              Tetromino.RIGHT: [(1, 1), (0, 1), (0, 2),
                                                (2, 1)],
                              Tetromino.DOWN: [(1, 1), (1, 0), (1, 2), (2, 2)],
                              Tetromino.LEFT: [(1, 1), (0, 1), (2, 1), (2, 0)],
                              Tetromino.UP: [(1, 1), (0, 0), (1, 0), (1, 2)],
                          }
                          ),
            # type L
            TetrominoType(orange,
                          {
                              Tetromino.RIGHT: [(1, 1), (0, 1), (2, 1),
                                                (2, 2)],
                              Tetromino.DOWN: [(1, 1), (1, 0), (1, 2), (2, 0)],
                              Tetromino.LEFT: [(1, 1), (0, 1), (2, 1), (0, 0)],
                              Tetromino.UP: [(1, 1), (1, 0), (1, 2), (0, 2)],
                          }
                          ),
            # type T
            TetrominoType(purple,
                          {
                              Tetromino.RIGHT: [(1, 1), (0, 1), (2, 1),
                                                (1, 2)],
                              Tetromino.DOWN: [(1, 1), (1, 2), (1, 0), (2, 1)],
                              Tetromino.LEFT: [(1, 1), (0, 1), (2, 1), (1, 0)],
                              Tetromino.UP: [(1, 1), (0, 1), (1, 0), (1, 2)],
                          }
                          ),
        ]

    @staticmethod
    def random_type():
        return random.choice(TetrominoType.TYPES)




# setpositionで指定したところにtetrominoをで生成できる？
class Tetromino(object):
    RIGHT, DOWN, LEFT, UP = range(4)
    CLOCKWISE_ROTATIONS = {RIGHT: DOWN, DOWN: LEFT, LEFT: UP, UP: RIGHT}

    def __init__(self, type=None):
        self.x = 0
        self.y = 0
        self.tetrominoType = TetrominoType.random_type()
        self.orientation = Tetromino.RIGHT
        self.blockBoardCoords = self.calc_block_board_coords()

    def calc_block_board_coords(self):
        local_block_coords = self.tetrominoType.localBlockCoordsByOrientation[
            self.orientation]
        grid_coords = []
        for coord in local_block_coords:
            grid_coord = (coord[0] + self.x, coord[1] + self.y)
            grid_coords.append(grid_coord)
        return grid_coords

    def get_block_coords(self):
        return self.blockBoardCoords

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.blockBoardCoords = self.calc_block_board_coords()

    def move_down(self):
        self.y -= 1
        self.blockBoardCoords = self.calc_block_board_coords()

    def move_up(self):
        self.y += 1
        self.blockBoardCoords = self.calc_block_board_coords()

    def move_left(self):
        self.x -= 1
        self.blockBoardCoords = self.calc_block_board_coords()

    def move_right(self):
        self.x += 1
        self.blockBoardCoords = self.calc_block_board_coords()

    def rotate_clockwise(self):
        self.orientation = Tetromino.CLOCKWISE_ROTATIONS[self.orientation]
        self.blockBoardCoords = self.calc_block_board_coords()

    def rotate_counterclockwise(self):
        self.orientation = Tetromino.CLOCKWISE_ROTATIONS[self.orientation]
        self.orientation = Tetromino.CLOCKWISE_ROTATIONS[self.orientation]
        self.orientation = Tetromino.CLOCKWISE_ROTATIONS[self.orientation]
        self.blockBoardCoords = self.calc_block_board_coords()

    def command(self, command):
        if command == Input.MOVE_DOWN:
            self.move_down()
        elif command == Input.MOVE_RIGHT:
            self.move_right()
        elif command == Input.MOVE_LEFT:
            self.move_left()
        elif command == Input.ROTATE_CLOCKWISE:
            self.rotate_clockwise()

    def undo_command(self, command):
        if command == Input.MOVE_DOWN:
            self.move_up()
        elif command == Input.MOVE_RIGHT:
            self.move_left()
        elif command == Input.MOVE_LEFT:
            self.move_right()
        #super rotation key point?
        elif command == Input.ROTATE_CLOCKWISE:
            self.rotate_counterclockwise()

    def clear_row_and_adjust_down(self, board_grid_row):
        new_block_board_coords = []
        for coord in self.blockBoardCoords:
            if coord[1] > board_grid_row:
                adjusted_coord = (coord[0], coord[1] - 1)
                new_block_board_coords.append(adjusted_coord)
            if coord[1] < board_grid_row:
                new_block_board_coords.append(coord)
        self.blockBoardCoords = new_block_board_coords
        return len(self.blockBoardCoords) > 0

    def draw(self, screen_coords):
        image = self.tetrominoType.blockImage
        for coords in screen_coords:
            image.blit(coords[0], coords[1])


class Board(object):
    STARTING_ZONE_HEIGHT = 4
    NEXT_X = -7
    NEXT_Y = 15
    playtimecount = 2
    judge = False
    Hold_count = 0
    Hard_judge = False

    tmp_x = 0
    tmp_y = 0

    SRS_tmp_x = 0
    SRS_tmp_y = 0

    def __init__(self, x, y, grid_width, grid_height, block_size, borad_image, queue):
        self.x = x
        self.y = y

        self._queue = queue

        self.BoradImage = borad_image

        self.gridWidth = grid_width
        self.gridHeight = grid_height
        self.blockSize = block_size
        self.spawnX = int(grid_width * 1 / 3)
        self.spawnY = grid_height
        self.nextTetromino = Tetromino()
        self.fallingTetromino = None
        self.spawn_tetromino()
        self.tetrominos = []
        self.tetromino_tmp = []

    # spo-n
    def spawn_tetromino(self):
        # self.fallingTetromino = self.nextTetromino
        # self.nextTetromino = Tetromino()
        # self.nextTetromino.set_position(Board.NEXT_X, Board.NEXT_Y)
        self.fallingTetromino = self._queue.next()
        self.fallingTetromino.set_position(self.spawnX, self.spawnY)
        self.Hold_count = 0

    def command_falling_tetromino(self, command):
        if not self.Hard_judge:
            self.fallingTetromino.command(command)
        # Harddrop function
        if command == Input.Harddrop:
            while self.is_valid_position():
                self.fallingTetromino.command(Input.MOVE_DOWN)
            self.fallingTetromino.move_up()
            self.playtimecount += 2
            self.Hard_judge = True
        #Hold function
        if command == Input.HOlD and self.Hold_count == 0:
            if len(self.tetromino_tmp) == 0:
                self.tetromino_tmp.append(self.fallingTetromino)
                self.spawn_tetromino()
            else:
                self.tmp_x = self.fallingTetromino.x
                self.tmp_y = self.fallingTetromino.y
                self.tetromino_tmp[0], self.fallingTetromino = self.fallingTetromino, self.tetromino_tmp[0]
                self.fallingTetromino.set_position(self.spawnX,self.spawnY)
            self.Hold_count += 1
        if not self.is_valid_position():
            # if command == Input.ROTATE_CLOCKWISE:
            #     self.SRS_tmp_x = self.fallingTetromino.x
            #     self.SRS_tmp_y = self.fallingTetromino.y
            #     if self.is_rotate():
            #         pass
            # else:
            self.fallingTetromino.undo_command(command)

    # def is_rotate(self):
    #     # X軸を　-1　して回転判定
    #     print("x-1")
    #     self.fallingTetromino.set_position(self.fallingTetromino.x - 1, self.fallingTetromino.y)
    #     self.fallingTetromino.command(Input.ROTATE_CLOCKWISE)
    #     if self.is_valid_position():
    #         print("kita")
    #         return True
    #     else:
    #         self.fallingTetromino.undo_command(Input.ROTATE_CLOCKWISE)
    #         self.fallingTetromino.command(Input.ROTATE_CLOCKWISE)
    #         self.fallingTetromino.set_position(self.SRS_tmp_x, self.SRS_tmp_y)
    #
    #     # X軸を　+1 して回転判定
    #     print("x+1")
    #     self.fallingTetromino.set_position(self.fallingTetromino.x + 1, self.fallingTetromino.y)
    #     self.fallingTetromino.command(Input.ROTATE_CLOCKWISE)
    #     if self.is_valid_position():
    #         print("kita")
    #         return True
    #     else:
    #         self.fallingTetromino.undo_command(Input.ROTATE_CLOCKWISE)
    #         self.fallingTetromino.command(Input.ROTATE_CLOCKWISE)
    #         self.fallingTetromino.set_position(self.SRS_tmp_x, self.SRS_tmp_y)
    #
    #     # Y軸を　-1 して回転判定
    #     print("y-1")
    #     self.fallingTetromino.set_position(self.fallingTetromino.x, self.fallingTetromino.y - 1)
    #     self.fallingTetromino.command(Input.ROTATE_CLOCKWISE)
    #     if self.is_valid_position():
    #         print("kita")
    #         return True
    #     else:
    #         self.fallingTetromino.undo_command(Input.ROTATE_CLOCKWISE)
    #         self.fallingTetromino.command(Input.ROTATE_CLOCKWISE)
    #         self.fallingTetromino.set_position(self.SRS_tmp_x, self.SRS_tmp_y)
    #
    #     # Y軸を +1 して回転判定
    #     print("y+1")
    #     self.fallingTetromino.set_position(self.fallingTetromino.x, self.fallingTetromino.y + 1)
    #     self.fallingTetromino.command(Input.ROTATE_CLOCKWISE)
    #     if self.is_valid_position():
    #         print("kita")
    #         return True
    #     else:
    #         self.fallingTetromino.undo_command(Input.ROTATE_CLOCKWISE)
    #         self.fallingTetromino.command(Input.ROTATE_CLOCKWISE)
    #         self.fallingTetromino.set_position(self.SRS_tmp_x, self.SRS_tmp_y)
    #         return False

    def is_valid_position(self):
        non_falling_block_coords = []
        for tetromino in self.tetrominos:
            non_falling_block_coords.extend(tetromino.blockBoardCoords)
        for coord in self.fallingTetromino.blockBoardCoords:
            out_of_bounds = coord[0] < 0 or coord[0] >= self.gridWidth or \
                            coord[1] < 0
            overlapping = coord in non_falling_block_coords
            if out_of_bounds or overlapping:
                return False
        return True

    def find_full_rows(self):
        non_falling_block_coords = []
        for tetromino in self.tetrominos:
            non_falling_block_coords.extend(tetromino.blockBoardCoords)

        row_counts = {}
        for i in range(self.gridHeight + Board.STARTING_ZONE_HEIGHT):
            row_counts[i] = 0
        for coord in non_falling_block_coords:
            row_counts[coord[1]] += 1

        #一列ごとのブロックの個数の判定
        full_rows = []
        for row in row_counts:
            if row_counts[row] == self.gridWidth:
                full_rows.append(row)
        return full_rows

    def clear_row(self, grid_row):
        tetrominos = []
        for tetromino in self.tetrominos:
            if tetromino.clear_row_and_adjust_down(grid_row):
                tetrominos.append(tetromino)
        self.tetrominos = tetrominos

    def clear_rows(self, grid_rows):
        grid_rows.sort(reverse=True)
        for row in grid_rows:
            self.clear_row(row)

    #infinity のための奴
    def press_key(self, symbol, modifiers):
        if symbol == (pyglet.window.key.LEFT or pyglet.window.key.RIGHT or pyglet.window.key.UP):
            self.judge = True
        else:
            self.judge = False
    def press_motion(self, motion):
        if motion == (pyglet.window.key.LEFT or pyglet.window.key.RIGHT or pyglet.window.key.UP):
            self.judge = True
        else:
            self.judge = False

    # konohen
    def update_tick(self):
        num_cleared_rows = 0
        game_lost = False
        #infinite function
        if self.judge:
            self.playtimecount = 0
            self.judge = False
        self.playtimecount += 1
        #print(self.playtimecount)
        if self.playtimecount > 2:
            self.fallingTetromino.command(Input.MOVE_DOWN)
        if not self.is_valid_position():
            self.fallingTetromino.undo_command(Input.MOVE_DOWN)
            self.tetrominos.append(self.fallingTetromino)
            full_rows = self.find_full_rows()
            self.clear_rows(full_rows)
            game_lost = self.is_in_start_zone(self.fallingTetromino)
            self.Hard_judge = False
            if not game_lost:
                self.spawn_tetromino()
            #クリアした列の数で点数を変える
            judge_rows = len(full_rows)
            if judge_rows == 4:
                num_cleared_rows = 8
            elif judge_rows == 3:
                num_cleared_rows = 5
            elif judge_rows == 2:
                num_cleared_rows = 2
            elif judge_rows == 1:
                num_cleared_rows = 1
            #num_cleared_rows = len(full_rows)
        return num_cleared_rows, game_lost

    #tetromino　がスタート地点にいるか確認する奴
    def is_in_start_zone(self, tetromino):
        for coords in tetromino.blockBoardCoords:
            if coords[1] >= self.gridHeight:
                return True
        return False

    #多分 1単位　Blocksizeにしてる奴
    def grid_coords_to_screen_coords(self, coords):
        screen_coords = []
        for coord in coords:
            coord = (self.x + coord[0] * self.blockSize,
                     self.y + coord[1] * self.blockSize)
            screen_coords.append(coord)
        return screen_coords

    #いろいろdrawしてるやつ
    def draw(self):
        self.BoradImage.blit(self.x - 3, self.y - 3)
        for tetromino in self.tetrominos:
            screen_coords = self.grid_coords_to_screen_coords(
                tetromino.blockBoardCoords)
            tetromino.draw(screen_coords)

        screen_coords = self.grid_coords_to_screen_coords(
            self.fallingTetromino.blockBoardCoords)
        self.fallingTetromino.draw(screen_coords)

        #Hold tetromino draw
        if not len(self.tetromino_tmp) == 0:
            self.tetromino_tmp[0].set_position(self.NEXT_X,self.NEXT_Y)
            screen_coords = self.grid_coords_to_screen_coords(
                self.tetromino_tmp[0].blockBoardCoords)
            self.tetromino_tmp[0].draw(screen_coords)

        #この辺に_queueに入っているtetrominoをdraw処理?
        self._queue.draw()

        # screen_coords = self.grid_coords_to_screen_coords(
        #     self.nextTetromino.blockBoardCoords)
        # self.nextTetromino.draw(screen_coords)


class InfoDisplay(object):
    ROWS_CLEARED_X = 70
    ROWS_CLEARED_Y = 550

    def __init__(self, window):
        self.rowsClearedLabel = pyglet.text.Label('Rows cleared: 0',
                                                  font_size=14,
                                                  x=InfoDisplay.ROWS_CLEARED_X,
                                                  y=InfoDisplay.ROWS_CLEARED_Y
                                                  )
        self.pausedLabel = pyglet.text.Label('PAUSED',
                                             font_size=32,
                                             x=window.width // 2,
                                             y=window.height // 2,
                                             anchor_x='center',
                                             anchor_y='center'
                                             )
        self.gameoverLabel = pyglet.text.Label('GAME OVER',
                                               font_size=32,
                                               x=window.width // 2,
                                               y=window.height // 2,
                                               anchor_x='center',
                                               anchor_y='center'
                                               )
        self.showPausedLabel = False
        self.showGameoverLabel = False

    def set_rows_cleared(self, num_rows_cleared):
        self.rowsClearedLabel.text = 'Rows cleared: ' + str(num_rows_cleared)

    def draw(self):
        self.rowsClearedLabel.draw()
        if self.showPausedLabel:
            self.pausedLabel.draw()
        if self.showGameoverLabel:
            self.gameoverLabel.draw()


class Input(object):
    TOGGLE_PAUSE, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT, ROTATE_CLOCKWISE, HOlD, Harddrop = range(7)
    playtime = 0

    def __init__(self):
        self.action = None

    def process_keypress(self, symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            self.action = Input.TOGGLE_PAUSE
        elif symbol == pyglet.window.key.ENTER:
            self.action = Input.HOlD
        elif symbol == pyglet.window.key.PAGEDOWN:
            self.action = Input.Harddrop

    def process_text_motion(self, motion):
        if motion == pyglet.window.key.MOTION_LEFT:
            self.action = Input.MOVE_LEFT
        elif motion == pyglet.window.key.MOTION_RIGHT:
            self.action = Input.MOVE_RIGHT
        elif motion == pyglet.window.key.MOTION_UP:
            self.action = Input.ROTATE_CLOCKWISE
        elif motion == pyglet.window.key.MOTION_DOWN:
            self.action = Input.MOVE_DOWN


    def consume(self):
        action = self.action
        self.action = None
        return action


class GameTick(object):
    def __init__(self, tick_on_first_call=False):
        self.tick = tick_on_first_call
        self.started = tick_on_first_call

    def is_tick(self, next_tick_time):
        def set_tick(dt):
            self.tick = True

        if not self.started:
            self.started = True
            pyglet.clock.schedule_once(set_tick, next_tick_time)
            return False
        elif self.tick:
            self.tick = False
            pyglet.clock.schedule_once(set_tick, next_tick_time)
            return True
        else:
            return False


class Game(object):
    def __init__(self, board, info_display, key_input, background_image):
        self.board = board
        self.infoDisplay = info_display
        self.input = key_input
        self.backgroundImage = background_image
        self.paused = False
        self.lost = False
        self.numRowsCleared = 0
        self.tickSpeed = 0.8
        self.ticker = GameTick()

    def add_rows_cleared(self, rows_cleared):
        self.numRowsCleared += rows_cleared
        self.infoDisplay.set_rows_cleared(self.numRowsCleared)
        self.SpeedUP(self.numRowsCleared)
        #print(self.tickSpeed)

    def toggle_pause(self):
        self.paused = not self.paused
        self.infoDisplay.showPausedLabel = self.paused

    def update(self):
        if self.lost:
            self.infoDisplay.showGameoverLabel = True

        else:
            command = self.input.consume()
            if command == Input.TOGGLE_PAUSE:
                self.toggle_pause()
            if not self.paused:
                if command and command != Input.TOGGLE_PAUSE:
                    self.board.command_falling_tetromino(command)
                if self.ticker.is_tick(self.tickSpeed):
                    rows_cleared, self.lost = self.board.update_tick()
                    self.add_rows_cleared(rows_cleared)

    #scoreに合わせてスピードアップ
    def SpeedUP(self, score):
        if score >= 25:
            self.tickSpeed = 0.05
        elif score >= 20:
            self.tickSpeed = 0.1
        elif score >= 15:
            self.tickSpeed = 0.2
        elif score >= 10:
            self.tickSpeed = 0.4
        elif score >= 5:
            self.tickSpeed = 0.6

    def draw(self):
        self.backgroundImage.blit(0, 0)
        self.board.draw()
        self.infoDisplay.draw()


class NextTetrominoQueue(object):
    """
    Nextブロックを管理するキュー
    """
    #位置調整用
    Next_Posi_X = 0
    Next_Posi_Y = 4
    Next_COUNT = 3

    def __init__(self, x, y, block_size, set_count):
        self._x = x
        self._y = y
        self._block_size = block_size
        self._set_count = set_count
        self._queue = deque()  # type: deque
        self.generate_tetromino()

    def generate_tetromino(self):
        """
        Tetrominoをset_countセット作ってシャッフルしてキューにぶち込む
        """
        tetromino_type_set = list(TetrominoType.TYPES[:] * self._set_count)
        for a in range(2):
            random.shuffle(tetromino_type_set)

        for tetromino_type in tetromino_type_set:
            self._queue.append(Tetromino(tetromino_type))

    def get(self, index):
        return self._queue[index]  # type: Tetromino

    #_queueから一番右側の要素を削除してそれを返す type:Tetromino型
    def next(self):
        if len(self._queue) < 5:
            self.generate_tetromino()
        return self._queue.popleft()  # type: Tetromino

    def grid_coords_to_screen_coords(self, coords):
        screen_coords = []
        for coord in coords:
            coord = (self._x + coord[0] * self._block_size,
                     self._y + coord[1] * self._block_size)
            screen_coords.append(coord)
        return screen_coords

    def draw(self):
        for i in range(self.Next_COUNT):
            self._queue[i].set_position(self.Next_Posi_X,self.Next_Posi_Y * (self.Next_COUNT - i - 1))
            screen = self.grid_coords_to_screen_coords(
                self._queue[i].get_block_coords())
            self._queue[i].draw(screen)

