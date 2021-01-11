import turtle

window = turtle.Screen()

colors=['red','purple','blue','green','yellow','orange']

t = turtle.Pen()
t.speed(0)
for x in range(3600):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

turtle.mainloop()
