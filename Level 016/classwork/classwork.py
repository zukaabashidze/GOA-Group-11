from turtle import* 
speed (3)
 
def draw_square():
    for i in range(4): 
        forward(100)
        left(90)

def move_cursor(x,y):
    penup()
    goto(x, y)
    pendown()

draw_square()
move_cursor(0, 300)

draw_square()
move_cursor(-300, 300)

draw_square()
move_cursor(-300, 0)

draw_square()
move_cursor(0, -300)

draw_square()
move_cursor(-300, 300)

draw_square

exitonclick()






