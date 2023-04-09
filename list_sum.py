def list_sum(l1: list, l2: list):
    return list(map(lambda x, y: x + y, l1, l2))


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))  # [8, 10, 12]
