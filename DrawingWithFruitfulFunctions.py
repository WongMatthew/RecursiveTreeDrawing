# Drawing using Fruitful Functions
# Author: Matthew
# Date: 19 November

import turtle
t = turtle.Turtle()
 
# Create a function tnhat returns x to the power of y
def power(x, y):
  return x ** y

# Create a function that draws a square
def draw_square(sidelen):
  for i in range(4):
    t.forward(sidelen)
    t.right(90)

# Use the two functions to draw increasingly larger squares
for i in range(12):
  draw_square(power(1.5, i))