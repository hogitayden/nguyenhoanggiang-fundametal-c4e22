from turtle import *

def draw_star(x, y, length):
    penup()
    setpos(x, y)
    pendown()
    left(36)
    for i in range(5):
        forward(length)
        left(144)

speed(0)
color_range = ["red", "blue", "yellow", "pink", "purple", "green"]  

for i in range(100):
    from random import *
    color(choice(color_range))
    x = randint(-300, 300)
    y = randint(-300, 300)
    length = randint(30, 100)
    draw_star(x, y, length)
mainloop()