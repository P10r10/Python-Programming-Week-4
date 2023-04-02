def line(n, s):
    to_print = "*" if s == "" else s[0]
    print(to_print * n)


def shape(ht, ct, hs, cs):
    for i in range(ht):
        line(i + 1, ct)
    for _ in range(hs):
        line(ht, cs)


if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")
