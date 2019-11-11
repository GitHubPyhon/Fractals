import turtle


ANGLE = 60
ITERATION = 3
PARTS = 3
LINE = 100 // (ITERATION * 3)


def seed(x):
    seed(x - 1) if x > 1 else t.forward(LINE)
    t.left(ANGLE)
    seed(x - 1) if x > 1 else t.forward(LINE)
    t.right(ANGLE * 2)
    seed(x - 1) if x > 1 else t.forward(LINE)
    t.left(ANGLE)
    seed(x - 1) if x > 1 else t.forward(LINE)


def main():
    for _ in range(PARTS):
        seed(ITERATION)
        t.right(360 / PARTS)


if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(speed=0)
    main()
    turtle.done()
