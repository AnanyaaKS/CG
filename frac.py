# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:39:24 2024

@author: anany
"""


import turtle
import math


def mandelbrot(z , c , n=20):
    if abs(z) > 10 ** 12:
        return float("nan")
    elif n > 0:
        return mandelbrot(z ** 2 + c, c, n - 1)
    else:
        return z ** 2 + c

# screen size (in pixels)
screenx, screeny = 800, 600

# complex plane limits
complexPlaneX, complexPlaneY = (-2.0, 2.0), (-1.0, 2.0)

# discretization step
step = 2

# turtle config
turtle.tracer(0, 0)
turtle.setup(screenx, screeny)

screen = turtle.Screen()
screen.bgcolor("red")
screen.title("Mandelbrot Fractal (discretization step = %d)" % (int(step)))
mTurtle = turtle.Turtle()
mTurtle.penup()
mTurtle.shape("square")

# px * pixelToX = x in complex plane coordinates
pixelToX, pixelToY = (complexPlaneX[1] - complexPlaneX[0])/screenx, (complexPlaneY[1] - complexPlaneY[0])/screeny

# plot
for px in range(-int(screenx/2), int(screenx/2), int(step)):
    for py in range(-int(screeny/2), int(screeny/2), int(step)):
        x, y = px * pixelToX, py * pixelToY
        m =  mandelbrot(0, x + 1j * y)
        if not math.isnan(m.real):
            color = [abs(math.sin(m.imag)) for i in range(3)]
            mTurtle.color(color)
            mTurtle.dot(2.4, color)
            mTurtle.goto(px, py)
    turtle.update()

turtle.mainloop()


'''
import turtle
import math

def julia(z, c, n=20):
    if abs(z) > 10 ** 12:
        return float("nan")
    elif n > 0:
        return julia(z ** 2 + c, c, n - 1)
    else:
        return z ** 2 + c

# screen size (in pixels)
screenx, screeny = 800, 600

# complex plane limits
complexPlaneX, complexPlaneY = (-2.0, 2.0), (-1.0, 2.0)

# discretization step
step = 2

# turtle config
turtle.tracer(0, 0)
turtle.setup(screenx, screeny)

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Julia Fractal (discretization step = %d)" % (int(step)))
jTurtle = turtle.Turtle()
jTurtle.penup()
jTurtle.shape("square")

# px * pixelToX = x in complex plane coordinates
pixelToX, pixelToY = (complexPlaneX[1] - complexPlaneX[0])/screenx, (complexPlaneY[1] - complexPlaneY[0])/screeny

# Julia set parameter (you can change this to create different Julia fractals)
c = complex(0.295, 0.55)

# plot
for px in range(-int(screenx/2), int(screenx/2), int(step)):
    for py in range(-int(screeny/2), int(screeny/2), int(step)):
        x, y = px * pixelToX, py * pixelToY
        j = julia(complex(x, y), c)
        if not math.isnan(j.real):
            color = [abs(math.sin(j.imag)) for i in range(3)]
            jTurtle.color(color)
            jTurtle.dot(2.4, color)
            jTurtle.goto(px, py)
    turtle.update()

turtle.mainloop()
'''

'''
import turtle

# Function to generate the Dragon Curve recursively
def dragon_curve(order, length, direction):
    if order == 0:
        turtle.forward(length)
        return
    else:
        dragon_curve(order - 1, length, 1)
        turtle.left(90 * direction)
        dragon_curve(order - 1, length, -1)
        return

# Main function to set up the turtle and draw the Dragon Curve
def draw_dragon_curve(order, length):
    turtle.speed(0)  # Set the turtle speed to the fastest
    turtle.penup()
    turtle.goto(-length * 2, 0)  # Set the starting position
    turtle.pendown()
    dragon_curve(order, length, 1)  # Draw the Dragon Curve
    turtle.done()

# Set the order and length of the Dragon Curve
order = 11  # Change the order for a more detailed curve (increase for more detail)
length = 5  # Change the length of each segment

# Set up the turtle graphics window
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Dragon Curve (order = %d)" % order)

# Draw the Dragon Curve
draw_dragon_curve(order, length)

'''

'''
#c- curve

from turtle import *
color('red', 'yellow')
begin_fill()
rule=['r','f','l','l','f','r']
prev=['r','f','l','l','f','r']
ans=[]
for iter in range(4):
    ans = []
    for i in prev:
        if(i=='f'):
            ans+=rule
        else:
            ans.append(i)
    prev = ans

print(ans)

for i in range(0,len(ans)):
    if(ans[i] == 'r'):
        right(45)
    elif(ans[i] == 'f'):
        forward(20)
    elif(ans[i] == 'l'):
        left(45)


end_fill()
done()
'''
'''
#cantor set

import numpy as np
import matplotlib.pyplot as plt

line = [0,1]
depth = 5

def divide(line, level=0):
    plt.plot(line,[level,level], color="k", lw=5, solid_capstyle="butt")
    if level < depth:
        s = np.linspace(line[0],line[1],4)
        divide(s[:2], level+1)
        divide(s[2:], level+1)

divide(line)
plt.gca().invert_yaxis()
plt.show()
'''

'''
#DRAGON CURVE

from turtle import *
color('red')
rule=['f','x']
prev=['f','x']
ans=[]
x_app = ['x','+','y','f','+']
y_app = ['-','f','x','-','y']

for iter in range(7):
    ans = []
    for i in prev:
        if(i=='x'):
            ans+=x_app
        elif(i=='y'):
            ans+=y_app
        else:
            ans.append(i)
    prev = ans

#print(ans)

for i in range(0,len(ans)):
    if(ans[i] == '+'):
        right(90)
    elif(ans[i] == '-'):
        left(90)
    elif(ans[i] == 'f'):
        forward(20)

done()
'''
'''
import turtle
import random
n=int(input("number of iterations of the terrain (give less than 10 ):-"))
#try to give the iterations as even numbers to see symmetry
# powers of 2 are more prefereable
step=float(input("step length for forward propagation :- "))
#adjust this step value to increase the size of the curve
#note as you increase the number of intersections , decrease the forward step value

"""
L system used :- 
variables : F
constants : + *
start  : F
rules  : (F -> F+F*F+F)
angle  : 60°,120°
Here, F means "draw forward", + means "turn left by angle" , and * means turn right by 120 deg
"""
def generate_string(n):
    if n == 0:
        return "F"
    else:
        prev_string = generate_string(n-1)
        new_string = ""
        for char in prev_string:
            if char == "F":
                new_string += "F+F*F+F"
            else:
                new_string += char
        return new_string
draw_string=generate_string(n)
print(len(draw_string))
turtle.penup()
turtle.goto(-150, -150)#starting pos of turtle to draw the curve
turtle.pendown()
turtle.speed(1000000)#speed of drawing can be still increased
for i in draw_string:
    if i=='F':
        color = (random.random(), random.random(), random.random())  # Random RGB color
        turtle.color(color)
        turtle.forward(step)
    elif i=='+':
        turtle.left(60)
    elif i=='*':
        turtle.right(120)
turtle.done()
 '''   
