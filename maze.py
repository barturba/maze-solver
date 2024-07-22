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

            # Check adjacent cells.
            # Make sure we're within the bounds of the maze
            if j - 1 >= 0:
                # add the cell above to the to_check list
                if not self._cells[i][j - 1]._visited:
                    to_visit.append((i, j - 1))
            if j + 1 < self.num_rows:
                # add the cell below to the to_check list
                if not self._cells[i][j + 1]._visited:
                    to_visit.append((i, j + 1))
            if i - 1 >= 0:
                # add the cell to the left to the to_check list
                if not self._cells[i - 1][j]._visited:
                    to_visit.append((i - 1, j))
            if i + 1 < self.num_cols:
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
            direction = to_visit[random.randrange(0, len(to_visit))]

            # Knock down the walls between the current cell and the chosen cell.
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

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j]._visited = False

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j]._visited = True

        # return true if the current cell is an end cell or if it leads to the end cell
        #  1. check if cell is an end cell
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        # #  2. check if current cell leads to the end cell
        # if (i == self.num_cols - 2 and j == self.num_rows - 1) or (
        #     i == self.num_cols - 1 and j == self.num_rows - 2
        # ):
        # return True

        # for each direction

        # up
        # Check if there's a cell in that direction
        if j - 1 >= 0:
            # Check if there's no wall blocking you
            if (
                not self._cells[i][j].has_top_wall
                and not self._cells[i][j - 1].has_bottom_wall
            ):
                # Check that the cell hasn't been visited
                if not self._cells[i][j - 1]._visited:
                    #  1. Draw a move between the current cell and thaht cell
                    self._cells[i][j].draw_move(self._cells[i][j - 1])
                    #  2. call _solve_r recursively to mowve to that cell. if that cell
                    #   returns True, then just return True and don't worry about the other
                    #   directions.
                    if self._solve_r(i, j - 1):
                        return True
                    #  3. Otherwise, draw an "undo" move between the current cell and the
                    #   next cell.
                    else:
                        self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # right
        # Check if there's a cell in that direction
        if i + 1 >= 0:
            # Check if there's no wall blocking you
            if (
                not self._cells[i][j].has_right_wall
                and not self._cells[i + 1][j].has_left_wall
            ):
                # Check that the cell hasn't been visited
                if not self._cells[i + 1][j]._visited:
                    #  1. Draw a move between the current cell and thaht cell
                    self._cells[i][j].draw_move(self._cells[i + 1][j])
                    #  2. call _solve_r recursively to mowve to that cell. if that cell
                    #   returns True, then just return True and don't worry about the other
                    #   directions.
                    if self._solve_r(i + 1, j):
                        return True
                    #  3. Otherwise, draw an "undo" move between the current cell and the
                    #   next cell.
                    else:
                        self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # down
        if j + 1 >= 0:
            # Check if there's no wall blocking you
            if (
                not self._cells[i][j].has_bottom_wall
                and not self._cells[i][j + 1].has_top_wall
            ):
                # Check that the cell hasn't been visited
                if not self._cells[i][j + 1]._visited:
                    #  1. Draw a move between the current cell and thaht cell
                    self._cells[i][j].draw_move(self._cells[i][j + 1])
                    #  2. call _solve_r recursively to mowve to that cell. if that cell
                    #   returns True, then just return True and don't worry about the other
                    #   directions.
                    if self._solve_r(i, j + 1):
                        return True
                    #  3. Otherwise, draw an "undo" move between the current cell and the
                    #   next cell.
                    else:
                        self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        # left

        # Check if there's a cell in that direction
        if i - 1 >= 0:
            # Check if there's no wall blocking you
            if (
                not self._cells[i][j].has_left_wall
                and not self._cells[i - 1][j].has_right_wall
            ):
                # Check that the cell hasn't been visited
                if not self._cells[i - 1][j]._visited:
                    #  1. Draw a move between the current cell and thaht cell
                    self._cells[i][j].draw_move(self._cells[i - 1][j])
                    #  2. call _solve_r recursively to mowve to that cell. if that cell
                    #   returns True, then just return True and don't worry about the other
                    #   directions.
                    if self._solve_r(i - 1, j):
                        return True
                    #  3. Otherwise, draw an "undo" move between the current cell and the
                    #   next cell.
                    else:
                        self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # if none of the directions worked out then return false
        return False

    def _solve(self):
        self._solve_r(0, 0)
