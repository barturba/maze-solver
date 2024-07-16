from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas()
        self.__canvas.pack()
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


def main():
    win = Window(800, 600)
    print("started window")
    win.wait_for_close()


if __name__ == "__main__":
    main()
