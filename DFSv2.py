#############################
# Depth First Search (DFS)
# Tony Davis
# 27.11.2018
#############################

import turtle                    # import turtle library
import time


wn = turtle.Screen()                      # define the turtle screen
wn.bgcolor("black")                       # set the background colour
wn.title("A Maze Solving Program")
wn.setup(1300,700)                        # setup the dimensions of the working window

# declare system variables
start_x = 0
start_y = 0
end_x = 0
end_y = 0

# the five classes below are drawing turtle images to construct the maze.

# use white turtle to stamp out the maze
class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("white")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)                   # define the animation speed

# use green turtles to show the visited cells
class Green(turtle.Turtle):               # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

# use blue turtle to show the frontier cells
class Blue(turtle.Turtle):               # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

# use the red turtle to represent the start position
class Red(turtle.Turtle):                # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.setheading(270)  # point turtle to point down
        self.penup()
        self.speed(0)

# use the yellow turtle to represent the end position and the solution path
class Yellow(turtle.Turtle):           # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

grid4 = [
    "+++++++++++++++",
    "              e",
    "               ",
    "               ",
    "               ",
    "               ",
    "               ",
    "               ",
    "s              ",
    "+++++++++++++++",
]

grid2 = [
"+++++++++++++++",
"+s+       + +e+",
"+ +++++ +++ + +",
"+ + +       + +",
"+ +   +++ + + +",
"+ + + +   + + +",
"+   + + + + + +",
"+++++ + + + + +",
"+     + + +   +",
"+++++++++++++++",
 ]

grid3 = [
"+++++++++",
"+ ++ ++++",
"+ ++ ++++",
"+ ++ ++++",
"+s   ++++",
"++++ ++++",
"++++ ++++",
"+      e+",
"+++++++++",
 ]

grid1 = [
"++++++++++++++++++++++++++++++++++++++++++++++",
"+ s             +                            +",
"+ +++++++++++ +++++++++++++++ ++++++++ +++++ +",
"+           +                 +        +     +",
"++ +++++++ ++++++++++++++ ++++++++++++++++++++",
"++ ++    + ++           + ++                 +",
"++ ++ ++ + ++ ++ +++++ ++ ++ +++++++++++++++ +",
"++ ++ ++ + ++ ++ +     ++ ++ ++ ++        ++ +",
"++ ++ ++++ ++ +++++++++++ ++ ++ +++++ +++ ++ +",
"++ ++   ++ ++             ++          +++ ++e+",
"++ ++++ ++ +++++++++++++++++ +++++++++++++++ +",
"++    + ++                   ++              +",
"+++++ + +++++++++++++++++++++++ ++++++++++++ +",
"++ ++ +                   ++          +++ ++ +",
"++ ++ ++++ ++++++++++++++ ++ +++++ ++ +++ ++ +",
"++ ++ ++   ++     +    ++ ++ ++    ++     ++ +",
"++ ++ ++ +++++++ +++++ ++ ++ +++++++++++++++ +",
"++                     ++ ++ ++              +",
"+++++ ++ + +++++++++++ ++ ++ ++ ++++++++++++++",
"++++++++++++++++++++++++++++++++++++++++++++++",
 ]

# this function constructs the maze based on the grid type above
def setup_maze(grid):                          # define a function called setup_maze
    global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
    for y in range(len(grid)):                 # iterate through each line in the grid
        for x in range(len(grid[y])):          # iterate through each character in the line
            character = grid[y][x]             # assign the variable character to the y and x positions of the grid
            screen_x = -588 + (x * 24)         # move to the x location on the screen staring at -288
            screen_y = 288 - (y * 24)          # move to the y location of the screen starting at 288

            if character == "+":                   # if character contains a '+'
                maze.goto(screen_x, screen_y)      # move pen to the x and y location and
                maze.stamp()                       # stamp a copy of the white turtle on the screen
                walls.append((screen_x, screen_y)) # add cell to the walls list

            if character == " ":                    # if no character found
                path.append((screen_x, screen_y))   # add to path list

            if character == "e":                    # if cell contains an 'e'
                yellow.goto(screen_x, screen_y)     # move pen to the x and y location and
                yellow.stamp()                      # stamp a copy of the yellow turtle on the screen
                end_x, end_y = screen_x, screen_y   # assign end locations variables to end_x and end_y
                path.append((screen_x, screen_y))   # add cell to the path list

            if character == "s":                       # if cell contains a "s"
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)           # send red turtle to start position

def search(x,y):
    frontier.append((x, y))                            # add the x and y position to the frontier list
    solution[x, y] = x, y                              # add x and y to the solution dictionary
    while len(frontier) > 0:                           # loop until the frontier list is empty
        time.sleep(0)                                  # change this value to make the animation go slower
        current = (x,y)                                # current cell equals x and  y positions

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check left
            cellleft = (x - 24, y)
            solution[cellleft] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(cellleft)        # blue turtle goto the  cellleft position
            blue.stamp()               # stamp a blue turtle on the maze
            frontier.append(cellleft)  # add cellleft to the frontier list

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check down
            celldown = (x, y - 24)
            solution[celldown] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(celldown)
            blue.stamp()
            frontier.append(celldown)

        if(x + 24, y) in path and (x + 24, y) not in visited:   # check right
            cellright = (x + 24, y)
            solution[cellright] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(cellright)
            blue.stamp()
            frontier.append(cellright)

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check up
            cellup = (x, y + 24)
            solution[cellup] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(cellup)
            blue.stamp()
            frontier.append(cellup)

        x, y = frontier.pop()           # remove last entry from the frontier list and assign to x and y
        visited.append(current)         # add current cell to visited list
        green.goto(x,y)                 # green turtle goto x and y position
        green.stamp()                   # stamp a copy of the green turtle on the maze
        if (x,y) == (end_x, end_y):     # makes sure the yellow end turtle is still visible after been visited
            yellow.stamp()              # restamp the yellow turtle at the end position 
        if (x,y) == (start_x, start_y): # makes sure the red start turtle is still visible after been visited
            red.stamp()                 # restamp the red turtle at the start position 

def backRoute(x, y):                       # this is the solution path function
    yellow.goto(x, y)                      
    yellow.stamp()
    while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
        yellow.goto(solution[x, y])        # move the yellow turtle to the key value of solution ()
        yellow.stamp()                     # create solution path
        x, y = solution[x, y]              # "key value" now becomes the new key

#  initialise lists
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()
walls = []
path = []
visited = []
frontier = []
solution = {}

setup_maze(grid1)                       # call setup maze function
search(start_x, start_y)                # call search function
backRoute(end_x, end_y)                 # call backroute function

wn.exitonclick()                        # exit out Pygame when x is clicked
