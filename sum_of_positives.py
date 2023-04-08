def sum_of_positives(lst: list):
    return sum(list(filter(lambda x: x > 0, lst)))


if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    print("The result is", sum_of_positives(my_list))
    my_list = [1, 2]
    print("The result is", sum_of_positives(my_list))
    sum_of_positives([1, 2])
