def everything_reversed(lst: list):
    return [n[::-1] for n in lst[::-1]]


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
