def line(n, s):
    to_print = "*" if s == "" else s[0]
    print(to_print * n)


def square(length, char):
    for _ in range(length):
        line(length, char)


if __name__ == "__main__":
    square(5, "*")
    print()
    square(3, "o")
