def line(n, s):
    to_print = "*" if s == "" else s[0]
    print(to_print * n)


def triangle(h):
    for i in range(h):
        line(i + 1, "#")


if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3)
