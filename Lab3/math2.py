# import calc
from calc import seasons #dau * la import tat ca function

x = int(input("x = "))
y = int(input("y = "))
op = input("Op (+ - * /): ")

# r = calc.seasons(x, y, op)
r = seasons(x, y, op)

print(x, op, y, "=", r)