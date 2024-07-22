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

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            to_visit = []
            can_check_above = False
            can_check_below = False
            can_check_left = False
            can_check_right = False

            # Check adjacent cells.
            # Make sure we're within the bounds of the maze
            if j - 1 >= 0:
                can_check_above = True
                # add the cell above to the to_check list
                if not self._cells[i][j - 1]._visited:
                    to_visit.append((i, j - 1))
            if j + 1 < self.num_rows:
                can_check_below = True
                # add the cell below to the to_check list
                if not self._cells[i][j + 1]._visited:
                    to_visit.append((i, j + 1))
            if i - 1 >= 0:
                can_check_left = True
                # add the cell to the left to the to_check list
                if not self._cells[i - 1][j]._visited:
                    to_visit.append((i - 1, j))
            if i + 1 < self.num_cols:
                can_check_right = True
                # add the cell to the right to the to_check list
                if not self._cells[i + 1][j]._visited:
                    to_visit.append((i + 1, j))

            # If there are zero directions you can go from the current cell,
            # then draw the current cell and return to break out of the loop.
            if len(to_visit) == 0:
                # draw the current cell
                # return
                self._draw_cell(i, j)
                return

            # Otherwise pick a random direction.
            # 0 up
            # 1 right
            # 2 down
            # 3 left
            direction = to_visit[random.randrange(0, len(to_visit))]
            # direction[0] - j > 0  = -1 (up), 1 (down), 0 none
            # direction[1] - i > 0 ? = -1 (left), 1 (right), 0 none

            # Know down the walls between the current cell and the chosen cell.
            # up
            if direction[1] - j < 0:
                # knock down top wall of current cell
                self._cells[i][j].has_top_wall = False
                # knock down bottom wall of chosen cell
                self._cells[i][direction[1]].has_bottom_wall = False
                self._break_walls_r(i, direction[1])
            # right
            elif direction[0] - i > 0:
                # knock down right wall of current cell
                self._cells[i][j].has_right_wall = False
                # knock down left wall of chosen cell
                self._cells[direction[0]][j].has_left_wall = False
                self._break_walls_r(direction[0], j)
            # down
            elif direction[1] - j > 0:
                # knock down bottom wall of current cell
                self._cells[i][j].has_bottom_wall = False
                # knock down top wall of chosen cell
                self._cells[i][direction[1]].has_top_wall = False
                self._break_walls_r(i, direction[1])
            # left
            else:
                # knock down left wall of current cell
                self._cells[i][j].has_left_wall = False
                # knock down right wall of chosen cell
                self._cells[direction[0]][j].has_right_wall = False
                self._break_walls_r(direction[0], j)
