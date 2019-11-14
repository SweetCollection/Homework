import turtle as t


def flower():
    t.pencolor("red")
    for i in range(6):
        t.begin_fill()
        t.fillcolor("pink")
        t.circle(5)
        t.left(60)
        t.end_fill()
        
        
def leaves():
    t.pencolor("green")
    t.begin_fill()
    t.fillcolor("green")
    t.circle(20,120)
    t.left(60)
    t.circle(20,120)
    t.end_fill()
    t.left(60)


def tree(n):
    t.pencolor("brown")
    if n > 0:
        t.pendown()
        t.forward(n)
        leaves()
        t.right(20)
        tree(n - 15)
        t.left(40)
        tree(n - 15)
        t.right(20)
        if n == 20:
            flower()
            t.penup()
        t.bk(n)
        
        
def main():
    t.pensize(2)
    t.speed(10)
    t.left(90)
    t.penup()
    t.goto(0,-150)
    t.pendown()
    tree(80)
    t.hideturtle()
 
 
if __name__ == "__main__":
    main()
