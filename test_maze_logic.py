import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):

    def test_break_walls_r(self):
        num_cols = 5
        num_rows = 5
        win = Window(800, 600)
        m1 = Maze(50, 50, num_rows, num_cols, 20, 20, 20, win)
        
        # Call the recursive break walls method from the top-left corner (0, 0)
        m1._break_walls_r(0, 0)
        
        # Check that the top-left cell has been visited (or walls have been broken)
        self.assertTrue(m1._cells[0][0].visited)
        
        # You can add more checks here to verify other specific walls are broken
        # For example, checking if a neighboring cell has been visited
        self.assertTrue(m1._cells[1][0].visited)  # Assuming some cells are visited in the recursion

        win.wait_for_close()

    def test_maze_solver(self):
        num_cols = 5
        num_rows = 5
        win = Window(800, 600)
        m1 = Maze(50, 50, num_rows, num_cols, 20, 20, 20, win)
        m1._break_walls_r(0,0 )
        m1._solve()
        m1._animate()
    
        win.wait_for_close()

if __name__ == "__main__":
    unittest.main()

"""     def test_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(50, 50, num_rows, num_cols, 10, 10, 42, win)
        
        # Initially mark some cells as visited
        m1._cells[3][3].visited = True
        m1._cells[6][6].visited = True
        
        # Now reset the visited status of all cells
        m1._reset_cells_visited()
        
        # Check that all cells have their visited status reset to False
        for col in m1._cells:
            for cell in col:
                self.assertFalse(cell.visited)
        
        win.wait_for_close() """

"""     def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)        
        m1 = Maze(50, 50, num_rows, num_cols, 10, 10, win)
        m1._break_entrance_and_exit()
        m1._animate()
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall, False)
        win.wait_for_close() """