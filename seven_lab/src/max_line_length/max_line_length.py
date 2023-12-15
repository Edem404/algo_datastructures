import math

args = "argument_file.txt"


def read_file(path_to_file):
    with open(path_to_file, 'r') as file:
        w = int(file.readline().strip())
        heights_str = file.readline().strip().split()
        heights = [int(num) for num in heights_str]
    return w, heights


def write_to_file(result_file, result):
    with open(result_file, 'w') as file:
        file.write(result)


def max_wire_length(args_path):
    args_from_file = read_file(args_path)
    w = args_from_file[0]
    heights = args_from_file[1]
    memoization = dict()

    def max_wire_length_calculate(first_in_pair, second_in_pair):
        current_combination = (first_in_pair, second_in_pair)
        if current_combination in memoization:
            return memoization[current_combination]

        if first_in_pair >= len(heights) - 1:
            return 0

        current_combination_length = 0
        for i in range(first_in_pair + 1, len(heights)):
            for j in range(heights[i], 0, -1):
                if (i, j) in memoization:
                    wire_len = math.sqrt(w ** 2 + (second_in_pair - j) ** 2) + memoization[(i, j)]
                else:
                    wire_len = math.sqrt(w ** 2 + (second_in_pair - j) ** 2) + max_wire_length_calculate(i, j)

                current_combination_length = max(current_combination_length, wire_len)

        memoization[current_combination] = current_combination_length
        return current_combination_length

    length_sum = max_wire_length_calculate(0, heights[0])
    write_to_file("result.txt", str(int(length_sum * 100) / 100.0))
    return int(length_sum * 100) / 100.0
