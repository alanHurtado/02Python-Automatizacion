import turtle, time

s= turtle.Screen()
t= turtle.Turtle()

s.bgcolor('black')
s.title('Prueba Tutle')
t.shapesize(3,3,3)
t.fillcolor('white')
t.pencolor('pink')

t.backward(100)
t.rt(90)
t.fd(100)
t.lt(90)
t.bk(100)
t.goto(100,100)
t.home()
t.clear()
t.goto(100,100)
t.goto(100,100)
t.home()
t.clear()

t.dot(20)
t.circle(50)

turtle.done()