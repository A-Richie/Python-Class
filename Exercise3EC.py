from ezgraphics import GraphicsWindow
from math import pi

# Alyssa Richie
# CIS 41A Python Programming 50Z
# Gets user input for a size of a circle and new window
# then makes a graphical window and draws a circle on the screen
# and prints the circumference and area of the circle

#Get width and height and makes the canvas and window
width = float(input("Enter a width for the graphics window: "))
height = float(input("Enter a height for the graphics window: "))
win = GraphicsWindow(width, height)
canvas = win.canvas()

#Set backgound color
canvas.setBackground(255, 255, 224)
#Sets title for graphics window
win.setTitle("CIS41A - Ch2 Ex3")

#Get radius for circle
radius = float(input("Enter a radius for a circle: "))

#Calculations for where the circle's center should be relative to canvas size
centerX = (width / 2) - radius
centerY = (height / 2) - radius

#Get specifications for the color for the cirle's inside and outline
outline = input("Enter the outline color for the circle: ")
fill = input("Enter the fill color for the circle: ")

#set width for line -- easier to see color of outline
canvas.setLineWidth(5)

#Sets the fill and outline from user input
canvas.setOutline(outline)
canvas.setFill(fill)

#Diameter for circle (used for calculations and drawing)
diameter = radius * 2

#Draws the circle on the window / canvas
canvas.drawOval(centerX, centerY, diameter, diameter)

#Set anchor for where text would be drawn (top left)
canvas.setTextAnchor("nw")

#Calculations for diameter and area
circumference = diameter * pi
area = pi * (radius ** radius)

#Creates one message, so only have to call drawText function once
message = "The circumference: " + str(circumference) + "\nThe area: " + str(area)
text_x = 0.01 * width
text_y = 0.01 * height

#Draws the text onto the graphic window
canvas.drawText(text_x , text_y , message)
print(message)

#Waits for user to close graphical window
win.wait()

'''
Output # 1 (And displays graphic window)
Enter a width for the graphics window: 500
Enter a height for the graphics window: 500
Enter a radius for a circle: 50
Enter the outline color for the circle: blue
Enter the fill color for the circle: green
The circumference: 314.1592653589793
The area: 2.7902947984069054e+85

Output # 2 (And displays graphic window)
Enter a width for the graphics window: 350
Enter a height for the graphics window: 600
Enter a radius for a circle: 120
Enter the outline color for the circle: red
Enter the fill color for the circle: purple
The circumference: 753.9822368615503
The area: 9.974689796304605e+249

'''