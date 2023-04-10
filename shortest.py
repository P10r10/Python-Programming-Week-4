def shortest(names: list):
    return min(names, key=len)


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    print(shortest(my_list))
    my_list2 = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    print(shortest(my_list2))
