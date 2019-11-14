import turtle as t

def snow(length,n):
    if n == 0:
        t.fd(length)
    else:
        for i in [0,60,-120,60]:
            t.left(i)
            snow(length/3, n-1)

def main():
    length = 500
    times = 4
    angle = 120
    t.pensize(3)
    t.color("blue")
    t.penup()
    t.goto(-150,150)   
    t.pendown()

    snow(length,times)
    t.right(angle)
    snow(length,times)
    t.right(angle)
    snow(length,times)
    t.right(angle)
    t.hideturtle()

main()
