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

    # def test_maze_break_entrance_and_exit(self):
    #     num_cols = 2
    #     num_rows = 9
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
    #     self.assertEqual(m1._cells[0][0].has_top_wall, False)
    #     self.assertEqual(m1._cells[num_cols - 1][num_rows - 1].has_right_wall, False)


if __name__ == "__main__":
    unittest.main()
