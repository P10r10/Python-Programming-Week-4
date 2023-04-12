# Please write a function named most_common_character, which takes a string argument.
# The function returns the character which has the most occurrences within the string.
# If there are many characters with equally many occurrences, the one which appears first
# in the string should be returned.

def most_common_character(s: str):
    res = s[0]
    for c in s:
        if s.count(c) > s.count(res):
            res = c
    return res


if __name__ == "__main__":
    first_string = "abcdbde"
    second_string = "exemplaryelementary"
    print(most_common_character(first_string))
    print(most_common_character(second_string))
