

def generate_quiz():
    import calc
    from random import randint, choice
    x = randint(0, 10)
    y = randint(1, 10)
    op = ["+", "-", "*", "/"]
    op = choice(op)
    error = randint(-1, 1)
    r = calc.seasons(x, y, op) + error
    return [x, op, y, r, error]