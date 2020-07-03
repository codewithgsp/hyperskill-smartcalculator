from string import asc
def last_indexof_max(numbers):
    # write the modified algorithm here
    max_val = 0
    index = -1

    for i, val in enumerate(numbers):
        if i == 0:
            max_val = val
            index = i
        elif val >= max_val:
            max_val = val
            index = i
    return index
