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


# def is_monotonous(arr):
#     increase = decrease = True
#     for i in range(1, len(arr)):
#         if arr[i - 1] > arr[i]:
#             increase = False
#         elif arr[i - 1] < arr[i]:
#             decrease = False
#
#     print()
#     print(increase)
#     print(decrease)
#
#
# is_monotonous([1, 2, 3, 4, 5])
# is_monotonous([5, 4, 3, 2, 1])
# is_monotonous([1, 4, 2, 5, 6, 7])
# is_monotonous([1, 2, 3, 3, 4, 5])
