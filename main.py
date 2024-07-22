from graphics import Window
from maze import Maze


def main():
    win = Window(810, 610)
    print("started window")

    m = Maze(5, 5, 10, 10, 800 // 10, 600 // 10, win)
    m._break_walls_r()

    win.wait_for_close()


if __name__ == "__main__":
    main()
