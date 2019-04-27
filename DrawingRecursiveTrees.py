# Recursive Tree
# Author: Matthew Wong
# Date: 14 November
# Use recursion to draw trees

import turtle

def draw_tree(level, branch_length):
  """
  A recursive function to draw trees
  level - num of levels of branches
  branch_length - length of branch in pixels
  """

  # Dictionary containing colour key-value pairs
  palette = {
    "spring": "#F9C6FF",
    "autumn": "#F78E67",
    "fall":   "#F78E67",
    "summer": "#549954",
    "winter": "#BCE5FF"
  }

  # If the level is 0 (leaf level)
  if level == 0:
    # Stamp the leaf
    turtle.color(palette["winter"])
    turtle.stamp()
    turtle.color("brown")
  # else we're at a branch level
  else:
    # 1. Draw a branch
    turtle.forward(branch_length)
    # 2. a. Turn left
    turtle.left(46)
    #    b. Draw a minitree
    draw_tree(level - 1, branch_length / 1.61)
    # Draw a middle branch
    turtle.right(46)
    draw_tree(level - 1, branch_length / 1.61)
    # 3. a. Turn right
    turtle.right(46)
    #    b. Draw a minitree
    draw_tree(level - 1, branch_length / 1.61)
    # 4. Go back
    turtle.left(46)
    turtle.back(branch_length)

# -------------------- Actual Code Under Here

# Setup the turtle
turtle.left(90)
turtle.speed(0)
turtle.penup()
turtle.goto(0, -180)
turtle.pendown()
# Setup the drawing
turtle.color("brown")
turtle.width(3)
turtle.shape("turtle")

# Draw the tree
draw_tree(4, 120)