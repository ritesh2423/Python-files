import turtle # allows us to use the turtles library

wn = turtle.Screen() # creates a graphics window
wn.setup(400,400) # set window dimension

circle_rad=50 # set
rectangle_width=150 #
rectangle_height=100 #

alex = turtle.Turtle() # create a turtle named alex
alex.shape("square") # alex looks like a turtle
alex.color('green') # alex has a color
'''alex.circle(circle_rad)
alex.backward(rectangle_width/2)
alex.forward(rectangle_width)
alex.left(90)
alex.forward(rectangle_height)
alex.left(90)
alex.forward(rectangle_width)
alex.left(90)
alex.forward(rectangle_height)'''
for i in range(1,4):
    alex.circle(i*10)
alex.left(120)
alex.color("red")
for i in range(1,4):
    alex.circle(i*10)
alex.left(120)
alex.color("blue")
for i in range(1,4):
    alex.circle(i*10)