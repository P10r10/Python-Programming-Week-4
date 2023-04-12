# Please write a function named most_common_character, which takes a string argument.
# The function returns the character which has the most occurrences within the string.
# If there are many characters with equally many occurrences, the one which appears first
# in the string should be returned.

def most_common_character(s: str):
    chars = []
    max_count = 0
    res = ""
    for c in s:
        if c not in chars:
            chars.append(c)
    for c in chars:
        if s.count(c) > max_count:
            max_count = s.count(c)
            res = c
    return res


if __name__ == "__main__":
    first_string = "abcdbde"
    second_string = "exemplaryelementary"
    print(most_common_character(first_string))
    print(most_common_character(second_string))
