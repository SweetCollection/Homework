import turtle as t

def flower(r):
    for i in range(6):
        t.circle(r)
        t.left(60)
 
    r -= 20
    if r > 0:
        flower(r)
        t.hideturtle()


def main():
    t.pencolor("pink")
    t.pensize(3)
    r = 50
    flower(100)

main()
