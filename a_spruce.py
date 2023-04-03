def spruce(height):
    print("a spruce!")
    for i in range(height):
        print(" " * (height - i - 1), end="")
        print("*" * (2 * i + 1))
    print(" " * (height - 1) + "*")  # trunk


if __name__ == "__main__":
    spruce(3)
    spruce(5)
