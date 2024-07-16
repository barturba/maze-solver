from graphics import Point, Line, Window


def main():
    win = Window(800, 600)
    print("started window")
    win.draw_line(Line(Point(0, 0), Point(800, 600)), "green")
    win.draw_line(Line(Point(400, 250), Point(600, 250)), "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
