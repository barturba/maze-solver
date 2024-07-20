import time
from graphics import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
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
