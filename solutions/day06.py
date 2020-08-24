from string import punctuation


def clean_string_solution(string):
    for p in punctuation:
        string = string.replace(p, "")
    return string