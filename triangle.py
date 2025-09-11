import sys

import turtle

def draw_triangle():
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)

def main():
    draw_triangle()

    return 0


if __name__ == "__main__":
    sys.exit(main())
