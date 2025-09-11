import sys

import turtle

def draw_pentagon():
    for i in range(5):
        turtle.forward(100)
        turtle.left(72)

def main():
    draw_pentagon()
    return 0
if __name__ == '__main__':
    sys.exit(main())