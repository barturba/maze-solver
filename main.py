from graphics import Cell, Point, Line, Window


def main():
    win = Window(800, 600)
    print("started window")
    c = Cell(win)
    d = Cell(win)

    d.draw(50, 50, 100, 100)

    c.draw(300, 300, 500, 500)
    c.draw_move(d, True)

    win.wait_for_close()


if __name__ == "__main__":
    main()
