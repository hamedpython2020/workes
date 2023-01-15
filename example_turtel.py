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
x1, y1 = (-10, 10)              #X1#
x2, y2 = (-1*i, i)              #X2#
x3, y3 = (110, 10)              #X3#
x4, y4 = (100+i, i)             #X4#
x5, y5 = (110, -10)             #X5#
x6, y6 = (100+i, -1*i)          #X6#
x7, y7 = (-10, -10)             #X7#
x8, y8 = (-1*i, -1*i)           #X8#
d2 = (i+100+i) / 10
d1 = ((-2*x1) + 100) / 10
print(x1, y1, x2, y2)
print(x3, y3, x4, y4)
print(x5, y5, x6, y6)
print(x7, y7, x8, y8)
n = 0
dx1 = 0
dx2 = 0
tr.goto(x2, y2)
#################Top join######################
helper = 0
while n <= 10:
    n += 1
    if n % 2 != 0:
        tr.fd(helper)
        tr.color("blue")
        tr.goto(x1+dx1, y1)
    else:
        tr.fd(d1)
        tr.color("purple")
        tr.goto(x2 + dx2, y2)
        pass
    tr.color("white")
    dx1 += d1
    dx2 += d2
    helper = d2
    pass
#################Down join######################
helper, n = (0, 0)
dy3, dy4 = (0, 0)
tr.right(90)
while n <= 10:
    n += 1
    if n % 2 != 0:
        tr.color("blue")
        tr.goto(x3, y3-dy3)
        tr.fd(d1)
        pass
    else:
        tr.color("purple")
        tr.goto(x4, y4-dy4)
        tr.fd(d2)
        pass
    tr.color("white")
    dy3 += d1
    dy4 += d2

    pass