def mean(lst: list):
    return sum(lst) / len(lst)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print("mean value is", result)
    my_list = [3, 6, -4]
    result = mean(my_list)
    print("mean value is", result)
    my_list = [1, 3, 67, 7, 4, 23, 1, 5, 7, 4]
    result = mean(my_list)
    print("mean value is", result)
