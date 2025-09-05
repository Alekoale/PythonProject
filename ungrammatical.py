import sys


def main():
    name = input("please enter your name: ")
    if name.istitle():
        print(" my name is " + name)

        return 0


if __name__ == "__main__":
        sys.exit(main())
