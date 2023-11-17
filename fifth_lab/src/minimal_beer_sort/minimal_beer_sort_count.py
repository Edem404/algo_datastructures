def read_file(param_file):
    """
        reading file and getting param
    :param param_file: path to file
    :return: tuple of params need for solve problem in func
    """
    with open(param_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        count_of_workers = int(lines[0].strip())
        beer_sort_count = int(lines[1].strip())
        yes_or_no = lines[2].strip('')
        yes_or_no = yes_or_no.replace(" ", "")

    return count_of_workers, beer_sort_count, yes_or_no


def create_dict(param_file):
    N, B, input_string = read_file(param_file)
    my_dict = {}

    for i in range(N):
        start_index = i * B
        end_index = (i + 1) * B
        substring = input_string[start_index:end_index]
        my_dict[i + 1] = substring

    return my_dict


def minimal_beer_sort_count(param_file):
    work_on_dictionary = create_dict(param_file)

    sorted_dict = dict(sorted(work_on_dictionary.items(), key=lambda x: (x[1].count("Y"))))
    processed_workers = set()
    types_of_beer = set()

    for key, value in sorted_dict.items():
        if key not in processed_workers and value.index("Y") + 1 not in types_of_beer:
            sort_liked_by_worker = [i + 1 for i, x in enumerate(value) if x == "Y"]
            print(f"Worker {key} likes sorts {sort_liked_by_worker}")

            chosen_sort = sort_liked_by_worker[len(sort_liked_by_worker) - 1]
            types_of_beer.add(chosen_sort)

    print(f"types of beer {types_of_beer}")
    print(f" {processed_workers}")
    print(sorted_dict)
    return len(types_of_beer)
