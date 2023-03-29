def line(n, s):
    to_print = "*" if s == "" else s[0]
    print(to_print * n)


if __name__ == "__main__":
    line(7, "%")
    line(10, "LOL")
    line(3, "")
