import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 32
        num_cols = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cols(self):
        num_rows = 45
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_rows(self):
        num_rows = 2
        num_cols = 9
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_rows = 2
        num_cols = 9
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[num_cols - 1][num_rows - 1].has_right_wall, False)

    def test_break_walls_r(self):
        num_rows = 2
        num_cols = 9
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        m1._break_walls_r(0, 0)

    def test_reset_cells_visited(self):
        num_rows = 2
        num_cols = 9
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        m1._break_walls_r(0, 0)
        m1._reset_cells_visited()
        all_cells_reset = True
        for i in range(num_cols):
            for j in range(num_rows):
                if m1._cells[i][j]._visited is True:
                    all_cells_reset = False
        self.assertEqual(all_cells_reset, True)


if __name__ == "__main__":
    unittest.main()
