def longest_series_of_neighbours(lst: list):
    count = 1
    max_count = 1
    i = 0
    while i < len(lst) - 1:
        if abs(lst[i] - lst[i + 1]) == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 1
        i += 1
    return max_count


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
