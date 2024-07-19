import time
from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        left = Line(top_left, bottom_left)
        right = Line(top_right, bottom_right)
        top = Line(top_left, top_right)
        bottom = Line(bottom_left, bottom_right)
        if self.has_left_wall:
            self._win.draw_line(left, "red")
        if self.has_right_wall:
            self._win.draw_line(right, "red")
        if self.has_top_wall:
            self._win.draw_line(top, "red")
        if self.has_bottom_wall:
            self._win.draw_line(bottom, "red")

    def draw_move(self, to_cell, undo=False):
        color = "gray"
        if undo:
            color = "red"
        center_x = self._x1 - ((self._x1 - self._x2) / 2)
        center_y = self._y1 - ((self._y1 - self._y2) / 2)

        other_center_x = to_cell._x1 - ((to_cell._x1 - to_cell._x2) / 2)
        other_center_y = to_cell._y1 - ((to_cell._y1 - to_cell._y2) / 2)
        line = Line(Point(center_x, center_y), Point(other_center_x, other_center_y))
        self._win.draw_line(line, color)


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
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

    def _create_cells(self):
        for col in range(self.num_rows):
            col_cells = []
            for row in range(self.num_cols):
                cell = Cell(self.win)
                col_cells.append(cell)
            self._cells.append(col_cells)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x = self._x1 + (i * self.cell_size_x + 1)
        y = self._y1 + (j * self.cell_size_y + 1)
        self._cells[j][i].draw(x, y, x + self.cell_size_x, y + self.cell_size_y)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
