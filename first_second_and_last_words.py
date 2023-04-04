def first_word(s):
    return s.split(" ")[0]


def second_word(s):
    return s.split(" ")[1]


def last_word(s):
    return s.split(" ")[-1]


if __name__ == "__main__":
    sentence = "it was a dark and stormy python"
    print(first_word(sentence))  # it
    print(second_word(sentence))  # was
    print(last_word(sentence))  # python
