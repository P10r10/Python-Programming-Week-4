def most_common_character(s: str):
    my_set = set(s)
    print("myset", my_set)
    lst = [s.count(c) for c in my_set]
    return lst


if __name__ == "__main__":
    first_string = "abcdbde"
    print(list(map(lambda x: first_string.count(x), first_string)))

# TODO
