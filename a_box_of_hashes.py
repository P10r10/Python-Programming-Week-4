def line(n, s):
    to_print = "*" if s == "" else s[0]
    print(to_print * n)


def box_of_hashes(height):
    for _ in range(height):
        line(10, "#")


if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)
