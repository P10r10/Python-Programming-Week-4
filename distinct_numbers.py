def distinct_numbers(lst: list):
    return sorted(list(set(lst)))


if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))  # [1, 2, 3]
