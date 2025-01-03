"""
Cell object of of the maze. Represents the indivudal blocks
which composes the maze.

"""
from graphics import Point, Line

class Cell():
    """
    Represents an individual square cell on the canvas. 
    It's four walls, four corners and reference to the window 
    """
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.visited = False
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")           
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")    
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        if (
            self._x1 is None or self._y2 is None or self._x2 is None or self._y2 is None or 
            to_cell._x1 is None or to_cell._y2 is None or to_cell._x2 is None or to_cell._y2 is None
        ):
            return 
        
        x_center = (self._x1 + self._x2) / 2
        y_center = (self._y1 + self._y2) / 2
        to_cell_center_x = (to_cell._x1 + to_cell._x2) / 2
        to_cell_center_y = (to_cell._y1 + to_cell._y2) / 2
        
        if self._win:
            line = Line(Point(x_center, y_center), Point(to_cell_center_x, to_cell_center_y))
            fill_color = "red" if not undo else "grey"
            self._win.draw_line(line, fill_color=fill_color)

