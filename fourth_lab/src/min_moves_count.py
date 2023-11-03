"""
    solution of chess knight minimum moves problem
"""
import collections
COUNT_OF_POSSIBLE_MOVES = 8


def read_file(param_file):
    """
        reading file and getting param
    :param param_file: path to file
    :return: tuple of params need for solve problem in func min_moves_count()
    """
    with open(param_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        board_size = int(lines[0].strip())
        start_position = tuple(map(int, lines[1].strip().split(",")))
        end_position = tuple(map(int, lines[2].strip().split(",")))

    return board_size, start_position, end_position


def write_file(path_to_result, moves):
    with open(path_to_result, "w", encoding="utf-8") as result_file:
        result_file.write(f"{moves}")


def min_moves_count(param_file, path_to_result):
    """
        function what solve problem about chess knight minimum moves using bfs

        time complexity - count of vertexes * count of edges.
        Edge = possible moves of knight (8)
        Vertex = cell of chess board
        So time complexity -> V * E or 8 * E or E(if it is possible to use=)
    :param param_file: path to file with arguments
    :param path_to_result: path to file with result
    :return: moves: INT minimal count of moves need to reach target cell on chess board
    """
    board_size, start_position, target_position = read_file(param_file)

    possible_moves_x = [2, 2, -2, -2, 1, 1, -1, -1]
    possible_moves_y = [-1, 1, 1, -1, 2, -2, 2, -2]

    visited = set()
    queue = collections.deque()

    visited.add(start_position)
    queue.append((start_position, 0))
    while queue:
        current_position, moves = queue.popleft()

        if current_position == target_position:
            write_file(path_to_result, moves)
            return moves

        for move in range(COUNT_OF_POSSIBLE_MOVES):
            current_x = current_position[0] + possible_moves_x[move]
            current_y = current_position[1] + possible_moves_y[move]

            if (
                0 <= current_x < board_size
                and 0 <= current_y < board_size
                and (current_x, current_y) not in visited
            ):
                visited.add((current_x, current_y))
                queue.append(((current_x, current_y), moves + 1))

    return None
