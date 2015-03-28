import turtle

brad = turtle.Turtle()
brad.shape('arrow')
brad.speed(0)

def fractal(color, size, pensize):
    brad.color(color)
    brad.pensize(pensize)
    for i in range(36):
        brad.right(10)
        for i in range(5):
            brad.right(72)
            brad.forward(size)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('black')
    fractal('white',120,2)
    fractal('blue',100,3)
    fractal('red',80,4)


    window.exitonclick()

draw_art()
