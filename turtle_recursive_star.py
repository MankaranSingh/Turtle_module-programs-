import turtle
pointer=turtle.Turtle()
pointer.up()
pointer.backward(100)
pointer.left(90)
pointer.forward(50)
pointer.right(90)
pointer.down()
def star(n):
    if n>10:
        pointer.left(70)
        pointer.forward(n)
        
        pointer.right(140)
        pointer.forward(n)
        pointer.left(70)
        pointer.forward(n)
        star(n/3)
        pointer.right(150)
        pointer.forward(n)
        pointer.left(75)
        pointer.forward(n)
        star(n/3)
        pointer.right(150)
        pointer.forward(n)
        pointer.left(95)
        pointer.forward(n)
        star(n/3)
        pointer.right(150)
        pointer.forward(n)
        pointer.left(75)
        pointer.forward(n)
        star(n/3)
        pointer.right(155)
        pointer.forward(n)
        
    
    

def main():
    star(300)

if __name__=='__main__':
    main()
