from turtle import *
import math

speed(0)
circle = Turtle()
shape("turtle")

def polygon(t, n, length):
    for i in range(n):
        left(360/n)
        forward(length)

def draw_circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

for i in range(10):
    draw_circle(circle, 100)
    left(7)

mainloop()