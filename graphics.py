"""
This uses tkinter to draw a visual representation of a maze.
Their is a single window that has a canvas, upon which all the drawing is done to create the waze.
The canvas/window is a cartesian plane with the top left corner being (0,0), and 
the maximal points (bottom left (y-axis) and top right (x-axis)).
This represents the current resolution of the computer screen. 
i.e... 3840 x 2160p (4k) / 1920 x 1080p (HD) 
"""

from tkinter import Tk, BOTH, Canvas

class Window():
    """
    Creates a window object, upon which a white canvas is created to draw the maze.
    """
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
   
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window has been closed...")
        
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False
        
class Point():
    """
    Point object to represent an x, y coordinate on a cartesian plane.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line():
    """
    Line object to represent the creation and connection of two point coordinates on a cartesian plane.
    """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)