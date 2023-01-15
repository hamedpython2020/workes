import turtle as tr

# tr.fd(100)
# tr.right(90)
# tr.fd(100)
# tr.right(90)
# tr.fd(100)
# tr.right(90)
# tr.fd(100)
# tr.color("white")
# tr.setpos(0, 25)
# tr.color("red")
# tr.rt(90)
# tr.fd(125)
# tr.right(90)
# tr.fd(150)
# tr.right(90)
# tr.fd(150)
# tr.right(90)
# tr.fd(150)
# tr.right(90)
# tr.fd(25)
# tr.color("white")
# tr.setpos(0, 50)
# tr.color("green")
# tr.fd(150)
# tr.right(90)
# tr.fd(200)
# tr.right(90)
# tr.fd(200)
# tr.right(90)
# tr.fd(200)
# tr.right(90)
# tr.fd(50)

i = 0
tr.speed(10)
while True:
    if i == 100:
        break
    tr.color("white")
    i += 10
    z = i / 10
    tr.setpos(0, i)
    if z % 3 == 0:
        tr.color("green")
    elif z % 2 == 0:
        tr.color("red")
    else:
        tr.color("orange")
    tr.fd(100 + i)
    tr.right(90)
    tr.fd(100 + 2*i)
    tr.right(90)
    tr.fd(100 + 2*i)
    tr.right(90)
    tr.fd(100 + 2*i)
    tr.right(90)
    tr.fd(i)
    pass
    ##################### drow Finish ########################
x2, y2 = (-1*i, i)
x1, y1 = (-10, 10)
dx2 = (i+100+i) / 10
dx1 = ((-2*x1) + 100) / 10
print(x1, y1, x2, y2)
n = 0
d1 = 0
d2 = 0
tr.goto(x2, y2)
#################Top join######################
helper = 0
while n <= 10:
    n += 1
    if n % 2 != 0:
        tr.fd(helper)
        tr.color("blue")
        tr.goto(x1+d1, y1)
    else:
        tr.fd(dx1)
        tr.color("purple")
        tr.goto(x2 + d2, y2)
        pass
    tr.color("white")
    d1 += dx1
    d2 += dx2
    helper = dx2
    pass
#################Down join######################
# helper = 0
# tr.goto(x2,-1*y2)
# yd1 = -1 * y1
# yd2 = -1*y2
# n = 0
# while n <= 10:
#     n += 1
#     if n % 2 != 0:
#         tr.fd(helper)
#         tr.color("blue")
#         tr.goto(x1+d1, yd1)
#     else:
#         tr.fd(dx1)
#         tr.color("purple")
#         tr.goto(x2 + d2, yd2)
#         pass
#     tr.color("white")
#     d1 += dx1
#     d2 += dx2
#     helper = dx2
#     pass
