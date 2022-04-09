# Rainbow Spiral Helix
import turtle

turtle.bgcolor("black")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple']

euler = turtle.Turtle()
euler.speed(10)

for i in range(360):
  euler.color(colors[i % 6])
  euler.width(i // 100 + 1)
  euler.forward(i)
  euler.left(59)
  euler.left(59)

turtle.done()
