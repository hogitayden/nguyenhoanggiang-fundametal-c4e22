from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    t = choice(shapes)
    text = t['text']
    c = choice(shapes)
    color = c['color']
    # r = choice(shapes)
    # rect = r['rect']
    ran = randint(0, 1)
    gen_quiz = [text, color, ran]
    return gen_quiz
# gen_quiz = generate_quiz()
# print(gen_quiz)
from turtle import *
def mouse_press(x, y, text, color, quiz_type):
    gen_quiz = generate_quiz()
    text, color, quiz_type = gen_quiz
    setpos(x, y)
    if quiz_type == 0:
        if text == 'blue':
            if 20 <= x <= 120 and 60 <= y <= 160:
                return True
            else:
                return False
        elif text == 'red':
            if 140 <= x <= 240 and 60 <= y <= 160:
                return True
            else:
                return False
        elif text == 'yellow':
            if 140 <= x <= 240 and 80 <= y <= 180:
                return True
            else:
                return False
        elif text == 'green':
            if 140 <= x <= 240 and 80 <= y <= 180:
                return True
            else:
                return False
    elif quiz_type == 1:
        if color == '#3F51B5':
            if 20 <= x <= 120 and 60 <= y <= 160:
                return True
            else:
                return False   
        elif color == '#C62828':
            if 140 <= x <= 240 and 60 <= y <= 160:
                return True
            else:
                return False
        elif color == '#FFD600':
            if 140 <= x <= 240 and 80 <= y <= 180:
                return True
            else:
                return False
        elif color == '#4CAF50':
            if 140 <= x <= 240 and 80 <= y <= 180:
                return True
            else:
                return False

