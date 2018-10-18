# def hello():
#     for _ in range(3):
#         print("Hello world")
# hello()

# def sum(x, y):
#     print(x + y)
# sum(5, 6)

from turtle import *
def draw_square(length, color):
    pencolor(color)
    for i in range(4):
        forward(length)
        left(90)
    
speed(0)
for i in range(30):
    draw_square(i*5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()