def is_arr_monotonous(array, i=0):
    if len(array) == 0:
        return False

    if len(array) == 1:
        return True

    if array[i] <= array[i + 1]:
        i += 1
        if (i + 1) == len(array) - 1:
            return True

        if array[i] > array[i + 1]:
            return False
        return is_arr_monotonous(array, i)

    elif array[i] >= array[i + 1]:
        i += 1
        if (i + 1) == len(array) - 1:
            return True

        if array[i] < array[i + 1]:
            return False
        return is_arr_monotonous(array, i)

    else:
        return False
