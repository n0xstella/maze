import unittest
from maze import Maze

class MazeTests(unittest.TestCase):

    def test_break_walls_r(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=42, win=None)
        
        # Call the recursive break walls method from the top-left corner (0, 0)
        m1._break_walls_r(0, 0)

        # Check that all cells have been visited
        for col in range(num_cols):
            for row in range(num_rows):
                self.assertTrue(
                    m1._cells[col][row]._visited,
                    f"Cell at ({col}, {row}) was not visited."
                )

        # Verify no cell has more walls removed than allowed
        for col in range(num_cols):
            for row in range(num_rows):
                cell = m1._cells[col][row]
                wall_count = (
                    cell.has_top_wall +
                    cell.has_right_wall +
                    cell.has_bottom_wall +
                    cell.has_left_wall
                )
                self.assertTrue(
                    0 <= wall_count <= 3,
                    f"Cell at ({col}, {row}) has too many walls removed: {4 - wall_count}"
                )

        # Additional test: Check the entrance and exit walls
        self.assertFalse(m1._cells[0][0].has_top_wall, "Entrance not open.")
        self.assertFalse(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            "Exit not open."
        )

if __name__ == "__main__":
    unittest.main()