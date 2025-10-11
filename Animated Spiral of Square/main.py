import turtle, colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
turtle.colormode(255)

for i in range(100):
    c = colorsys.hsv_to_rgb(i/100,1,1)
    t.pencolor(int(c[0]*255), int(c[1]*255), int(c[2]*255))
    for _ in range(4):
        t.forward(i*3)
        t.right(90)
    t.right(15)

turtle.done()