# def shortest(lst: list[str]):
#     short = len(lst[0])
#     idx = 0
#     idx_short = 0
#     while idx < len(lst):
#         if len(lst[idx]) < short:
#             idx_short = idx
#             short = len(lst[idx])
#         idx += 1
#     return lst[idx_short]
def shortest(names: list):
    return min(names, key=len)


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    print(shortest(my_list))
    my_list2 = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    print(shortest(my_list2))
