import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 32
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cols(self):
        num_cols = 45
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_rows(self):
        num_cols = 2
        num_rows = 9
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )


if __name__ == "__main__":
    unittest.main()
