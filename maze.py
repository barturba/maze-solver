import random
import time
from graphics import Cell


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=0
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for col in range(self.num_cols):
            col_cells = []
            for row in range(self.num_rows):
                cell = Cell(self.win)
                col_cells.append(cell)
            self._cells.append(col_cells)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        line_width = 3
        x = self._x1 + (i * self.cell_size_x) + line_width
        y = self._y1 + (j * self.cell_size_y) + line_width
        self._cells[i][j].draw(x, y, x + self.cell_size_x, y + self.cell_size_y)
        self._animate()

    def _animate(self):
        if self.win is not None:
            self.win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        i = self.num_cols - 1
        j = self.num_rows - 1
        self._cells[i][j].has_right_wall = False
        self._draw_cell(i, j)

    def _break_walls_r(self):
        i = 0
        j = 0
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Check the cells that are directly adjacent to the current cell.
            # Keep track of any that have not been visited as "possible
            # directions" to move to
            #  0   1   2
            #  3  [4]  5
            #  6   7   8
            #
            # [0]>[1]  2
            #  3   4   5
            #  6   7   8
            #
            # check above
            # check below
            # check left
            # check right

            # check above
            # j - 1
            # if j - 1 == 0: OK
            # if j - 1 == 1: OK
            # if j - 1 == -1: NOT OK
            #
            # if j - 1` >= 0:
            # can_check_above = True`
            can_check_above = False
            can_check_below = False
            can_check_left = False
            can_check_right = False

            if j - 1 >= 0:
                can_check_above = True
            if j + 1 <= self.num_rows:
                can_check_below = True
            if i - 1 >= 0:
                can_check_left = True
            if i + 1 <= self.num_cols:
                can_check_right = True

        #     if i + 1 <= self.num_cols and not self._cells[i + 1][j]._visited:
        #         to_visit.append((i + 1, j))
        #     elif j + 1 <= self.num_cols and not self._cels[i][j + 1]._visited:
        #         to_visit.append((i, j + 1))
        #     if len(to_visit) == 0:
        #         # draw cell
        #         # return to break out of the loop
        #         return
        #     else:
        #         random.randrange()

        # for i in range(self.num_cols):
        #     for j in range(self.num_rows):
        #         # mark the current cell as visited
        #         self._cells[i][j].visited = True
