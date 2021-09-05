def spiral(times,angleSpace,length,breadth,color):
    import turtle
    spiral = turtle.Turtle()
    spiral.speed(10)
    spiral.fillcolor(color)
    spiral.begin_fill()
    for i in range(times):
        spiral.forward(length)
        spiral.right(10.5)
        spiral.forward(breadth)
        spiral.left(30)
        spiral.forward(breadth)
        spiral.right(30)   
        spiral.penup()
        spiral.setposition(0, 0)
        spiral.pendown()
        spiral.right(angleSpace)
    spiral.end_fill()
    turtle.done()
spiral(180,60,80,30,"#53a4a9")
# you can change all the parameters to see the changes.
