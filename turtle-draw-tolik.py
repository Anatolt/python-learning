import turtle

def draw_square(some_turtle):    
    for i in range (4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('green')
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('red')
    brad.pensize(10)
    brad.speed(2)
    brad.forward(100)
    brad.backward(50)
    brad.right(90)
    brad.forward(100)
    brad.color('green')
    brad.left(90)
    brad.forward(100)
    brad.color('red')
    brad.circle(50)
    brad.color('green')
    brad.forward(60)
    brad.color('red')
    brad.left(90)
    brad.forward(100)
    brad.backward(100)
    brad.right(90)
    brad.forward(50)
    brad.color('green')
    brad.forward(10)
    brad.color('red')
    brad.left(90)
    brad.forward(90)
    brad.color('green')
    brad.forward(10)
    brad.right(90)
    brad.color('red')
    brad.circle(10)
    brad.color('green')
    brad.forward(20)
    brad.color('red')
    brad.right(90)
    brad.forward(100)
    brad.backward(50)
    brad.left(45)
    hypotenuza = (50**2 + 45**2)**0.5
    brad.forward(hypotenuza)
    brad.backward(hypotenuza)
    brad.left(90)
    brad.forward(hypotenuza)
    window.exitonclick()

draw_art()
