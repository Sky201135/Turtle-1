import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("lightblue")
my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        my_pen.fd(size)
        my_pen.left(90)
    size = size + 5
turtle.done()