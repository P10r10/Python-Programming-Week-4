def all_the_longest(lst: list):
    longest = max(map(len, lst))
    return list(filter(lambda x: len(x) == longest, lst))


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)  # ['eleventh']
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)  # ['dorothy', 'richard']
