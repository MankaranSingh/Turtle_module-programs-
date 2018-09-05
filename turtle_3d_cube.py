import turtle
p=turtle.Turtle()
size=200
margin=size
while size>0.01:
    p.forward(size)
    p.left(90)
    p.forward(size)
    p.left(90)
    p.forward(size)
    p.left(90)
    p.forward(size)
    p.left(135)
    p.penup()
    p.forward(margin/50)
    p.pendown()
    p.right(45)
    size=size-2
 
    
