import functools


def sql_in_params(input):
    output = ""
    if isinstance(input, [list, tuple]):
        for item in input:
            output += "'" + item + "'"
        output.strip()
    return output