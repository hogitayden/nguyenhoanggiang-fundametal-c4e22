# def add(x, y):
#     r = x + y #khong nen de print trong def
#     return r

# a = int(input("a = "))
# b = int(input("b = "))

# t = add(a, b)  #day la noi r roi ra tu ham con

# print(a, "+", b, "=", t) 

def seasons(x, y, op):
    if op == "-" :
        r = x - y    #return x - y
    elif op == "+":
        r = x + y   
    elif op == "*":
        r = x*y  
    elif op == "/":
        r = x/y
    return r

