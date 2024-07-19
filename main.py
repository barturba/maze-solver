from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    print("started window")

    m = Maze(0, 0, 10, 10, 800 // 10, 600 // 10, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
