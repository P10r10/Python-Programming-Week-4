# def formatted(lst: list):
#     res = []
#     for n in lst:
#         res.append(f"{n:.2f}")
#     return res

# def formatted(lst: list):
#     return [f"{n:.2f}" for n in lst]

def formatted(lst: list):
    return list(map(lambda x: f"{x:.2f}", lst))


if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    print(formatted(my_list))
