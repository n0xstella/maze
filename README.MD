# Purpose of Self-Solving Maze  
Purpose was to just practice several programming skills related primarily to abstraction, inheritance, recursion. Also garnered a bit more familarity  
with the tkinkter module as well.  

As the title states, the goal was to have the maze auto-resolve. While solving it will create a grey line for failed paths taken,  
while also creating a red line for the corret one leading ot the maze exit.

## Maze Generation
Execution is simply running the main.py file. The maze can be modified by the listed variables below, located within the main function.

num_rows = total number of rows in the maze  

num_cols = total number of columns in in the maze  

margin = sets the position of the maze on the canvas  

screen_x = width of the naze on the canvas, although technically this an individual cell's width which contributes to the overall maze width  

screen_y = height of the maze on the canvas, although technically this an individual cell's height which contributes to the overall maze height  

win = defaults to 800x600 for the width and height of the window  

## Limitations
Maximum recursion is limited, as to not make your CPU overheat.  