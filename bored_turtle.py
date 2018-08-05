import turtle

turtle.speed(1000)
turtle.bgcolor('black')
colors = ['red','purple','blue','brown','yellow','green']
for i in range(10000):
    turtle.pencolor(colors[i%6])
    turtle.degrees()
    turtle.right(121)
    turtle.forward(i)

turtle.mainloop()
