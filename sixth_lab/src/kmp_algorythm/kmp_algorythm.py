"""
    Bordulyak Roman 6 lab 30.11.2023
    Realisation of Knuth–Morris–Pratt algorythm
    returning indexed of entry of needle(looking text)
"""


def prefix_function(founding_string):
    """
    creating prefix array of founding string
    :param founding_string:  what we are looking for
    :return: prefix_arr: prefix array
    """
    prefix_arr = [0] * len(founding_string)
    i = 0
    j = 1
    while j < len(founding_string):
        if founding_string[i] == founding_string[j]:
            prefix_arr[j] = i + 1
            i = i + 1
            j = j + 1
        else:
            if i == 0:
                prefix_arr[j] = 0
                j = j + 1
            else:
                i = prefix_arr[i - 1]

    return prefix_arr


def kmp(needle: str, haystack: str):
    """
    Knuth–Morris–Pratt algorythm what looking one or more entry of needle in haystack
    :param needle: text what we are looking for
    :param haystack: text in what we are searching
    :return: result: array of indexes of all needle`s entry
    """
    i_haystack = 0
    i_needle = 0

    prefix_arr = prefix_function(needle)
    result = []
    while i_haystack < len(haystack):
        if haystack[i_haystack] == needle[i_needle]:
            i_haystack = i_haystack + 1
            i_needle = i_needle + 1
            if i_needle == len(needle):
                result.append(i_haystack - len(needle))
                if i_needle > 0:
                    i_needle = prefix_arr[i_needle - 1]
        else:
            i_needle = prefix_arr[i_needle - 1]
            if i_needle == 0:
                i_haystack = i_haystack + 1

    return result
