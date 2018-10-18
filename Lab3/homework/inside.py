def is_inside(x, y):
    # print(y[0], x[0], y[0] + y[2])
    if y[0] <= x[0] <= y[0] + y[2] and y[1] <= x[1] <= y[1] + y[3]:
        return True
    else:
        return False
in_or_out1 = is_inside([100, 120], [140, 60, 100, 200])
in_or_out2 = is_inside([200, 120], [140, 60, 100, 200])
# print(in_or_out1, in_or_out2)
if in_or_out1 == False and in_or_out2 == True:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")