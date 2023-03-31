def line(n, s):
    to_print = "*" if s == "" else s[0]
    print(to_print * n)


def square_of_hashes(side):
    for _ in range(side):
        line(side, "#")


if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)
