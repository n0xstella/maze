import unittest
from maze import  Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 6
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 5, 5)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
if __name__ == "__main__":
    unittest.main()